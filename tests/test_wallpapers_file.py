import pytest

from space_walls.wallpapers_file import WallpapersFile


def test_wallpapers_file(fixture_file):
    """
    WHEN: a WallpapersFile object is instantiated with no path
    THEN: it should still work
    """
    file = WallpapersFile()
    assert file

def test_wallpapers_file_wallpapers(fixture_file):
    """
    GIVEN: a valid wallpapers file
    WHEN: .wallpapers is called
    THEN: the list of wallpapers should be returned
    """
    json_file = fixture_file("wallpapers.json")

    file = WallpapersFile(json_file)
    wallpapers = file.wallpapers

    assert isinstance(wallpapers, dict)


@pytest.mark.skip
def test_wallpapers_file_wallpapers_invalid(fixture_file):
    """
    GIVEN: something about .data that doesn't match our expectatios
    WHEN: when .wallpapers is called
    THEN:a SpacesFileError should be raised
    """
