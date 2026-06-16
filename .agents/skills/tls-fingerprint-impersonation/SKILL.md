---
name: tls-fingerprint-impersonation
description: Diagnose and fix HTTP requests that fail (403, timeout, or connection reset) against CDN-protected APIs that block standard Python clients via TLS/JA3 fingerprinting. Use when adding or debugging outbound HTTP to ClinicalTrials.gov or any upstream where httpx/requests are silently rejected but a browser or curl works.
---

# TLS Fingerprint Impersonation

## Overview

Some CDNs (Akamai-, Cloudflare-, and Imperva-style protection) fingerprint the
TLS ClientHello — the ordering of cipher suites and extensions, known as a
**JA3 fingerprint** — to identify the client library. They allowlist real
browsers and reject everything else, regardless of HTTP headers. Standard
Python HTTP clients (`httpx`, `requests`, `aiohttp`) all present a recognizable
non-browser fingerprint and get blocked.

ClinicalTrials.gov's v2 API is one such upstream. The fix used in this repo is
to make requests with `curl_cffi`, which impersonates a real browser's TLS
handshake. See `src/clinicaltrials/utils.py`.

## Symptoms — when to use this skill

- `httpx` / `requests` / `aiohttp` calls return **403**, **hang/time out**, or
  get a **connection reset**, while the *same URL* works in a browser or `curl`.
- Setting a browser `User-Agent` header does **not** fix it. This is the key
  tell: the block is at the TLS layer, not the HTTP-header layer, so header
  spoofing can't help.
- The failure is network-dependent (works from some networks, not others) or
  appears intermittently as the CDN tunes its rules.

## Root cause

During the TLS handshake the client sends a ClientHello whose cipher
suites and extension ordering are characteristic of the library that produced
it. The CDN hashes this into a JA3 fingerprint and compares it against an
allowlist of real browsers. Because the fingerprint is determined by the TLS
stack — not by anything in the HTTP request — you cannot change it by setting
headers or a User-Agent. You must make the TLS handshake itself look like a
browser.

## The fix (canonical pattern)

Use [`curl_cffi`](https://github.com/lexiforest/curl_cffi), which wraps a
patched libcurl that can mimic browser TLS fingerprints via `impersonate`.

Async (as used by the MCP tools — `src/clinicaltrials/utils.py:7-13`):

```python
from curl_cffi.requests import AsyncSession

def make_api_client() -> AsyncSession:
    """Async client that impersonates Chrome's TLS fingerprint.

    ClinicalTrials.gov's CDN uses TLS fingerprint (JA3) blocking that rejects
    standard Python HTTP clients. Impersonating Chrome bypasses this.
    """
    return AsyncSession(impersonate="chrome")
```

Sync equivalent for non-async contexts:

```python
from curl_cffi.requests import Session

def make_api_client() -> Session:
    return Session(impersonate="chrome")
```

- `impersonate="chrome"` tracks a recent Chrome. You can pin a specific build
  (`"chrome120"`, etc.), but the generic `"chrome"` target is the
  lower-maintenance default — prefer it unless a specific upstream demands a
  pinned version.
- `curl_cffi`'s request API is close to `requests`/`httpx`:
  `.get(url, params=..., timeout=...)`, `.raise_for_status()`, `.json()`,
  `.text` all work as expected.

## Integration notes

- **Centralize the client in one factory.** Define a single
  `make_api_client()` and call it everywhere; don't scatter
  `AsyncSession(impersonate=...)` across the codebase. This keeps the
  impersonation target and TLS policy in one place.
- **Lifecycle.** This repo opens a client per request:

  ```python
  async with make_api_client() as client:
      response = await client.get(url, params=query_params, timeout=30.0)
      response.raise_for_status()
  ```

  That is simple and correct, but creates a new connection each call (no
  pooling). Under high load or for the paginating tools, a shared long-lived
  client is a reasonable alternative.

## Dependency

- Requires `curl_cffi>=0.14.0` (already in `pyproject.toml`). It bundles a
  patched libcurl, so there is **no** system `curl` dependency.
- **Tradeoff:** impersonation is inherently fragile. The bundled fingerprint
  must track current browser releases, and the CDN can change its policy at any
  time. This adds a supply-chain and maintenance burden — only take it on when
  fingerprint blocking is confirmed.

## Verification

1. Reproduce the block with a standard client, then confirm the fix:

   ```python
   # Fails / hangs against a fingerprint-blocking CDN:
   import httpx
   httpx.get("https://clinicaltrials.gov/api/v2/studies/NCT00000102")

   # Succeeds (HTTP 200):
   from curl_cffi.requests import Session
   r = Session(impersonate="chrome").get(
       "https://clinicaltrials.gov/api/v2/studies/NCT00000102"
   )
   assert r.status_code == 200
   ```

2. This is environment-sensitive — test from the actual deployment network, not
   just a local machine, since CDN behavior can differ by source network.

## When NOT to use this

- Don't reach for `curl_cffi` for ordinary APIs that work fine with `httpx` or
  `requests`. It is a heavier dependency with ongoing maintenance cost.
- Apply it only after confirming the failure is TLS-fingerprint blocking
  (browser/curl works, header-spoofed Python client still fails).
