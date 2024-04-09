"""Contains logic pertaining to JSON files."""

import json
from json.decoder import JSONDecodeError

from space_walls import SpaceWallsAccessError, SpaceWallsFileError
from space_walls.files.file import File


class JSONFile(File):
    """A JSON file."""
    @property
    def data(self):
        """Returned parsed data from JSON."""
        if not self.path:
            return

        with self.path.open() as fp:
            try:
                data = json.load(fp)
            except JSONDecodeError as e:
                raise SpaceWallsFileError(f"Invalid JSON formatting: {e}")

        return data

    @property
    def contents(self):
        """Return the file contents, but raise if the file is blank."""
        text = super().contents
        if not text:
            raise SpaceWallsFileError(f"File is blank: {self.path}")
        return text

