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
