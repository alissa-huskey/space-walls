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
    WHEN: db.images is accessed
    THEN: it should return all of the space_uuids and images
    """
    path = fixture_file("desktoppicture.db")
    db = WallpapersDB(path)
    images = db.images

    assert len(images) == 9


def test_wallpapers_db_():
    """
    GIVEN:
    WHEN: ...
    THEN: ...
    """

    db = WallpapersDB()
    assert db
