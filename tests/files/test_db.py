from contextlib import closing

import pytest

from space_walls.files.db import DB
from space_walls import SpaceWallsProgramError


def test_db():
    db = DB()
    assert db


def test_db_file(fixture_file):
    """
    """
    path = fixture_file("desktoppicture.db")
    db = DB(path)
    assert db.path == path


def test_db_connection_no_path():
    """
    GIVEN: DB object with no path
    WHEN: db.connection is accessed
    THEN: an exception should be raised
    """
    db = DB()

    with pytest.raises(SpaceWallsProgramError):
        with db.connection as conn:
            assert conn


def test_db_connection_with_path(fixture_file):
    """
    GIVEN: DB object with no path
    WHEN: the db.connection context manager is used
    THEN: an exception should be raised
    """
    path = fixture_file("desktoppicture.db")
    db = DB(path)

    with closing(db.connection) as conn:
        assert conn


def test_db_connection_with_path(fixture_file):
    """
    GIVEN: DB object with no path
    WHEN: the db.connection context manager is used
    THEN: an exception should be raised
    """
    path = fixture_file("desktoppicture.db")
    db = DB(path)

    with db.connection as conn:
        assert conn


def test_db_cursor(fixture_file):
    """
    GIVEN: DB object with path
    WHEN: the db.cursor context manager is used
    THEN: it should yield a cursor
    """
    path = fixture_file("desktoppicture.db")
    db = DB(path)

    with db.cursor as cur:
        assert cur


def test_db_select(fixture_file):
    """
    GIVEN: DB object with path
    WHEN: the db.select() is called
    THEN: it should return the results of the query
    """
    path = fixture_file("desktoppicture.db")
    db = DB(path)

    data = db.select("SELECT count(*) FROM data")

    assert len(data) == 1
    assert len(data[0]) == 1
    assert data[0][0] == 13
