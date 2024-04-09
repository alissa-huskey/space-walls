import pytest

from space_walls.files.spaces_file import SpacesFile


def test_spaces_file(fixture_file):
    """
    WHEN: a SpacesFile object is instantiated with no path
    THEN: it should still work
    """
    file = SpacesFile()
    assert file


def test_spaces_file_spaces(fixture_file):
    """
    WHEN: a SpacesFile object is instantiated with no path
    THEN: it should still work
    """
    path = fixture_file("com.apple.spaces.plist")
    file = SpacesFile(path)
    spaces = file.spaces

    assert isinstance(spaces, list)
    assert len(spaces) == 9
