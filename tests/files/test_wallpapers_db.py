from space_walls.files.wallpapers_db import WallpapersDB


def test_wallpapers_db():
    """
    WHEN: a WallpapersDB object is created
    THEN: it should work
    """

    db = WallpapersDB()
    assert db


def test_wallpapers_db_images(fixture_file):
    """
    GIVEN: A database populated with all the things
    WHEN: db.wallpapers is accessed
    THEN: it should return all of the space_uuids and images
    """
    path = fixture_file("desktoppicture.db")
    db = WallpapersDB(path)
    wps = db.wallpapers

    assert len(wps) == 9
