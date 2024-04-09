import pytest

from space_walls.files.json_file import JSONFile
from space_walls import SpaceWallsAccessError, SpaceWallsFileError


def test_json_file_data_invalid(fixture_file):
    """
    GIVEN: a file with invalid javascript
    WHEN: .data is called
    THEN: an exception should be raised
    """

    json_file = fixture_file("invalid.json")

    file = JSONFile(json_file)

    with pytest.raises(SpaceWallsFileError):
        file.data


def test_json_file_data_valid(fixture_file):
    """
    GIVEN: a file with invalid javascript
    WHEN: .data is called
    THEN: an exception should be raised
    """

    json_file = fixture_file("spaces.json")

    file = JSONFile(json_file)
    assert file.data


def test_json_file_contents_blank(fixture_file):
    """
    GIVEN: a JSON file with no text
    WHEN: it is set to .path
    THEN: it should raise an exception
    """
    json_file = fixture_file("blank.json")
    file = JSONFile(json_file)

    with pytest.raises(SpaceWallsFileError):
        assert not file.contents
