"""Contains logic pertaining to files."""

import json
from json.decoder import JSONDecodeError
from pathlib import Path

from space_walls import SpaceWallsAccessError, SpaceWallsFileError
from space_walls.attr import attr
from space_walls.object import Object


class File(Object):
    """A file."""

    def _validate_path(self, value):
        if not value:
            return
        path = Path(value)
        if not path.is_file():
            raise SpaceWallsAccessError(f"Unable to open file: {path}")

        if not (path.stat().st_size):
            raise SpaceWallsFileError(f"File is empty: {path}")

        self._path = path

    path = attr("path", setter=_validate_path)

    def __init__(self, path: Path=None):
        """Make a File object."""
        self.path = path
        self._data = None

    def __str__(self) -> str:
        """Print the path string if available."""
        if not self.path:
            return self.__repr__()
        return str(self.path)

    @property
    def contents(self):
        """Return the file contents."""
        if not self.path:
            return

        return self.path.read_text().strip()
