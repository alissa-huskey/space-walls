import pytest

from space_walls.files.spaces_json_file import SpacesJSONFile


def test_spaces_json_file():
    """
    WHEN: a SpacesJSONFile object is instantiated with no path
    THEN: it should still work
    """
    file = SpacesJSONFile()
    assert file

def test_spaces_json_file_spaces(fixture_file):
    """
    GIVEN: a valid spaces file
    WHEN: .spaces is called
    THEN: the list of spaces should be returned
    """
    json_file = fixture_file("spaces.json")

    file = SpacesJSONFile(json_file)
    spaces = file.spaces

    assert isinstance(spaces, dict)


@pytest.mark.skip
def test_spaces_json_file_spaces_invalid(fixture_file):
    """
    GIVEN: something about .data that doesn't match our expectatios
    WHEN: when .spaces is called
    THEN:a SpacesJSONFile should be raised
    """
