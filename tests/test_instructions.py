"""Tests for server instructions loading.

These verify that ``load_server_instructions`` resolves the bundled
``server_instructions.txt`` independently of the current working directory
(via ``importlib.resources``) and returns the expected content.
"""

import logging

import pytest

from clinicaltrials.instructions import load_server_instructions


def test_load_returns_nonempty_string():
    text = load_server_instructions()
    assert isinstance(text, str)
    assert text.strip() != ""


def test_load_contains_known_marker():
    text = load_server_instructions()
    assert "ClinicalTrials.gov MCP Server Instructions" in text


def test_load_is_cwd_independent(tmp_path, monkeypatch):
    """Loading must not depend on being run from the repo root."""
    monkeypatch.chdir(tmp_path)
    text = load_server_instructions()
    assert isinstance(text, str)
    assert "ClinicalTrials.gov MCP Server Instructions" in text


def test_warning_logged_when_missing(monkeypatch, caplog):
    """If the resource cannot be found, warn and return None (no raise)."""
    import clinicaltrials.instructions as instructions_module

    class _MissingResource:
        def joinpath(self, *_args, **_kwargs):
            return self

        def read_text(self, *_args, **_kwargs):
            raise FileNotFoundError

    monkeypatch.setattr(
        instructions_module, "files", lambda *_a, **_k: _MissingResource()
    )

    with caplog.at_level(logging.WARNING):
        result = load_server_instructions()

    assert result is None
    assert any(
        "server_instructions.txt" in record.message for record in caplog.records
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
