"""Tests for the platform v4.0 entry points."""

from core.platform_v_4_0 import run


def test_run_returns_status_message():
    """run should return the default status message."""
    assert run() == "Platform v4 running"
