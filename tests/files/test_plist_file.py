from pathlib import Path

import pytest

from space_walls.files.plist_file import PlistFile


def test_plist_file():
    """
    WHEN: a PlistFile object is instantiated with no path
    THEN: it should still work
    """
    file = PlistFile()
    assert file


def test_plist_data(fixture_file):
    """
    GIVEN: a SpacesPlist object
    WHEN: .data is accessed
    THEN: it should return the data parsed from the plist
    """
    #  plist_path = fixture_file("com.apple.spaces.plist")
    plist_path = Path.home() / "Library" / "Preferences" /  "com.apple.spaces.plist"
    file = PlistFile(plist_path)
    data = file.data

    assert isinstance(data, dict)
    assert "SpacesDisplayConfiguration" in data
