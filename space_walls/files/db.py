import sqlite3
from functools import cached_property
from contextlib import contextmanager

from space_walls.files.file import File
from space_walls import SpaceWallsProgramError


class DB(File):
    """A sqlite3 database."""
    def contents(self):
        """Noop"""

    @property
    @contextmanager
    def cursor(self):
        """A cursor for the database connection."""
        with self.connection as conn:
            cursor = conn.cursor()
            try:
                yield cursor
            finally:
                cursor.close()

    @property
    @contextmanager
    def connection(self):
        """A context manager for the database connection."""
        if not self.path:
            raise SpaceWallsProgramError("Cannot connect to database without a path.")

        conn = sqlite3.connect(self.path)

        try:
            yield conn
        finally:
            conn.close()

    def select(self, query, *params):
        with self.cursor as cur:
            cur.execute(query, params)
            data = cur.fetchall()

        return data
