import pytest

from space_walls.spaces_file import SpacesFile


def test_spaces_file(fixture_file):
    """
    WHEN: a SpacesFile object is instantiated with no path
    THEN: it should still work
    """
    file = SpacesFile()
    assert file

def test_spaces_file_spaces(fixture_file):
    """
    GIVEN: a valid spaces file
    WHEN: .spaces is called
    THEN: the list of spaces should be returned
    """
    json_file = fixture_file("spaces.json")

    file = SpacesFile(json_file)
    spaces = file.spaces

    assert isinstance(spaces, list)


@pytest.mark.skip
def test_spaces_file_spaces_invalid(fixture_file):
    """
    GIVEN: something about .data that doesn't match our expectatios
    WHEN: when .spaces is called
    THEN:a SpacesFileError should be raised
    """
