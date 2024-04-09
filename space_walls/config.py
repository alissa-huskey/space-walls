"""System configuration module."""

from itertools import chain

from .object import Object
from .spaces_file import SpacesFile
from .wallpapers_file import WallpapersFile


class Config(Object):
    """Stores the system configuration related to wallpapers."""

    def __init__(self, spaces_file = None, wallpapers_file = None):
        """Initialize config file.

        Arguments:
            spaces_file (Path): File that contains JSON file exported from com.apple.spaces.plist plist
            wallpapers_file (Path): File that contains the JSON
            """
        self.spaces_file = SpacesFile(spaces_file)
        self.wallpapers_file = WallpapersFile(wallpapers_file)

    @property
    def spaces(self):
        return self.spaces_file.spaces

    @property
    def wallpapers(self):
        return self.wallpapers_file.wallpapers

    @property
    def uuids(self):
        keys = set(chain(self.wallpapers.keys(), self.spaces.keys()))
        return sorted(list(keys))

    @property
    def images(self) -> dict:
        """Return a dictionary of desktop ID to image path."""
        space, wall = self.spaces, self.wallpapers

        images = {
            space[u]["ManagedSpaceID"]: wall[u]["wallpaper"]
            for u in self.uuids
            if u
        }
        images = dict(sorted(images.items(), key=lambda x: x[0]))
        return images

