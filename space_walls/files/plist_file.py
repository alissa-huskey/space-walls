"""Plist Files."""

import plistlib
from functools import cached_property
from pathlib import Path

from space_walls.files.file import File


class PlistFile(File):
    """Plist File class."""

    PLIST_FILE: Path = None
    """Default location of plist file."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.path = self.path or self.PLIST_FILE

    @cached_property
    def data(self):
        """Return the data loaded from the plist file."""
        with self.path.open("rb") as fp:
            data = plistlib.load(fp)
        return data
