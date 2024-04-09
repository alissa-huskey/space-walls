import plistlib
from functools import cached_property

from space_walls.files.file import File


class PlistFile(File):
    @cached_property
    def data(self):
        """Return the data loaded from the plist file."""
        with self.path.open("rb") as fp:
            data = plistlib.load(fp)
        return data

    def contents(self):
        """We don't really need the contents of the file, but making this a
        noop so that it doesn't cause problems."""
