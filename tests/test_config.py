from space_walls.config import Config


def test_config():
    """
    WHEN: a Config object is instantiated
    THEN: it should work
    """
    cfg = Config()
    assert cfg


def test_config_json_files(fixture_file):
    """
    GIVEN: a Config object
    WHEN: a spaces and/or wallpapers file is set
    THEN: the json should be loaded
    """
    spaces_file = fixture_file("spaces.json")
    wallpapers_file = fixture_file("wallpapers.json")

    cfg = Config(spaces_file, wallpapers_file)

    assert str(cfg.spaces_file) == str(spaces_file)
    assert str(cfg.wallpapers_file) == str(wallpapers_file)


def test_config_images(fixture_file):
    """
    GIVEN: valid spaces and wallpapers files
    WHEN: .images is caled
    THEN: a dictionary of desktop ID to image paths should be returned
    """

    spaces_file = fixture_file("spaces.json")
    wallpapers_file = fixture_file("wallpapers.json")
    image_path = "~/Library/Application Support/com.apple.mobileAssetDesktop/The Cliffs.heic"

    cfg = Config(spaces_file, wallpapers_file)

    data = cfg.images


    assert data
    assert len(data) == 8
    assert data.get(2, "") == image_path
