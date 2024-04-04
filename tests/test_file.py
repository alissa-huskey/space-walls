import pytest

from space_walls.file import File
from space_walls import SpaceWallsAccessError, SpaceWallsFileError


def test_file(fixture_file):
    """
    WHEN: a File object is instantiated with no path
    THEN: it should still work
    """
    file = File()
    assert file


def test_file_path_missing(fixture_file):
    """
    GIVEN: a Path object for a file that does not exist
    WHEN: it is set to .path
    THEN: it should raise an exception
    """
    json_file = fixture_file("config.json")

    with pytest.raises(SpaceWallsAccessError):
        File(json_file)


def test_file_path_empty(fixture_file):
    """
    GIVEN: a zero byte file
    WHEN: it is set to .path
    THEN: it should raise an exception
    """
    json_file = fixture_file("empty.json")

    with pytest.raises(SpaceWallsFileError):
        File(json_file)


def test_file_path_blank(fixture_file):
    """
    GIVEN: a JSON file with no text
    WHEN: it is set to .path
    THEN: it should raise an exception
    """
    json_file = fixture_file("blank.json")

    with pytest.raises(SpaceWallsFileError):
        File(json_file)


def test_file_path_valid(fixture_file):
    """
    GIVEN: a File object with a valid JSON file
    WHEN: .data is called
    THEN: it should work
    """
    json_file = fixture_file("spaces.json")

    file = File(json_file)
    assert file.path == json_file


def test_file_data_invalid(fixture_file):
    """
    GIVEN: a file with invalid javascript
    WHEN: .data is called
    THEN: an exception should be raised
    """

    json_file = fixture_file("invalid.json")

    file = File(json_file)

    with pytest.raises(SpaceWallsFileError):
        file.data


def test_file_data_valid(fixture_file):
    """
    GIVEN: a file with invalid javascript
    WHEN: .data is called
    THEN: an exception should be raised
    """

    json_file = fixture_file("spaces.json")

    file = File(json_file)
    assert file.data
