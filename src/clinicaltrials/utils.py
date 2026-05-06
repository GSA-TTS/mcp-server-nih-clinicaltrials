from curl_cffi.requests import AsyncSession
from curl_cffi.requests.exceptions import HTTPError, Timeout

CT_API_BASE_URL = "https://clinicaltrials.gov/api/v2"


def make_api_client() -> AsyncSession:
    """Return an async HTTP client that impersonates Chrome's TLS fingerprint.

    ClinicalTrials.gov's CDN uses TLS fingerprint (JA3) blocking that rejects
    standard Python HTTP clients. Impersonating Chrome bypasses this.
    """
    return AsyncSession(impersonate="chrome")


def _handle_api_error(e: Exception) -> str:
    """Return a clear, actionable error message for API failures."""
    if isinstance(e, HTTPError):
        status = e.response.status_code
        if status == 404:
            return "Error: Study not found. Verify the NCT ID is correct (e.g., 'NCT00000102')."
        if status == 400:
            return f"Error: Bad request — check your parameters. Details: {e.response.text}"
        if status == 429:
            return "Error: Rate limit exceeded. Please wait before retrying."
        return f"Error: API request failed with status {status}: {e.response.text}"
    if isinstance(e, Timeout):
        return "Error: Request timed out. Please try again."
    return f"Error: Unexpected error — {type(e).__name__}: {e}"
