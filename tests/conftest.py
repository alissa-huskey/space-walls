"""Test fixtures."""

from pathlib import Path

import pytest


@pytest.fixture
def testdir() -> Path:
    """Return the path to the root testing directory."""
    return Path(__file__).parent


@pytest.fixture
def fixturedir(testdir) -> Path:
    """Return the path to the fixture directory."""
    return testdir/"fixture_data"


@pytest.fixture
def fixture_file(fixturedir) -> Path:
    """Return a callable to get a fixture path."""
    def filepath(filename):
        """Return the path to a fixture file."""
        return fixturedir/filename
    return filepath
