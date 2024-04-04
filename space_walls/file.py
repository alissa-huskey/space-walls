"""."""

import json
from json.decoder import JSONDecodeError
from pathlib import Path

from . import SpaceWallsAccessError, SpaceWallsFileError
from .attr import attr
from .object import Object


class File(Object):
    """A JSON file."""

    def _validate_path(self, value):
        if not value:
            return
        path = Path(value)
        if not path.is_file():
            raise SpaceWallsAccessError(f"Unable to open file: {path}")

        self.contents = path.read_text().strip()

        if not (path.stat().st_size and self.contents):
            raise SpaceWallsFileError(f"Not a valid JSON file: {path}")

        self._path = path

    path = attr("path", setter=_validate_path)

    def __init__(self, path = None):
        """Make a File object."""
        self.path = path
        self._data = None

    def __str__(self):
        """Print the path string if available."""
        if not self.path:
            return self.__repr__()
        return str(self.path)

    @property
    def data(self):
        """Load data from JSON."""
        if not self.path:
            return

        with self.path.open() as fp:
            try:
                data = json.load(fp)
            except JSONDecodeError as e:
                raise SpaceWallsFileError(f"Invalid JSON formatting: {e}")

        return data
