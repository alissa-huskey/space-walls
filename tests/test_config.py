import pytest

from space_walls.config import Config


@pytest.mark.skip
def test_config():
    """
    WHEN: a Config object is instantiated
    THEN: it should work
    """
    cfg = Config()
    assert cfg


def test_config_files(fixture_file):
    """
    GIVEN: a Config object
    WHEN: a spaces and/or wallpapers file is set
    THEN: the json should be loaded
    """
    spaces_file = fixture_file("com.apple.spaces.plist")
    wallpapers_db = fixture_file("desktoppicture.db")

    cfg = Config(spaces_file, wallpapers_db)

    assert str(cfg.spaces_file) == str(spaces_file)
    assert str(cfg.wallpapers_db) == str(wallpapers_db)


def test_config_spaces(fixture_file):
    """
    GIVEN: a valid spaces plist file
    WHEN: .spaces is caled
    THEN: a dictionary of uuids to spaces should be returned
    """

    spaces_file = fixture_file("com.apple.spaces.plist")

    cfg = Config(spaces_file)
    data = cfg.spaces

    assert isinstance(data, dict)
    assert len(data) == 9


def test_config_wallpapers(fixture_file):
    """
    GIVEN: a valid desktoppictures.db file
    WHEN: .wallpapers is caled
    THEN: a dictionary of uuids to wallpapers should be returned
    """

    path = fixture_file("desktoppicture.db")

    cfg = Config(wallpapers_db=path)
    data = cfg.wallpapers

    assert isinstance(data, dict)
    assert len(data) == 9


def test_config_uuids(fixture_file):
    """
    GIVEN: valid spaces and wallpapers files
    WHEN: .uuids is caled
    THEN: a list of space_uuids from spaces file and wallpapers db should be returned
    """

    spaces_file = fixture_file("com.apple.spaces.plist")
    wallpapers_db = fixture_file("desktoppicture.db")

    cfg = Config(spaces_file, wallpapers_db)

    uuids = cfg.uuids

    assert isinstance(uuids, list)
    assert len(uuids) == 9


def test_config_images(fixture_file):
    """
    GIVEN: valid spaces and wallpapers files
    WHEN: .images is caled
    THEN: a dictionary of desktop ID to image paths should be returned
    """

    spaces_file = fixture_file("com.apple.spaces.plist")
    wallpapers_db = fixture_file("desktoppicture.db")
    image_path = "~/Library/Application Support/com.apple.mobileAssetDesktop/The Cliffs.heic"

    cfg = Config(spaces_file, wallpapers_db)
    data = cfg.images

    assert data
    assert len(data) == 9
    assert data[2].image_path == image_path
