"""System configuration module."""

from collections import namedtuple
from itertools import chain

from space_walls.files.spaces_file import SpacesFile
from space_walls.files.wallpapers_db import WallpapersDB
from space_walls.object import Object

Image = namedtuple("Image", ("space_number", "space_uuid", "data_id", "image_path"))


class Config(Object):
    """Stores the system configuration related to wallpapers."""

    def __init__(self, spaces_file=None, wallpapers_db=None):
        """Initialize config file.

        Arguments:
            spaces_file (Path): File that contains JSON file exported from com.apple.spaces.plist plist
            wallpapers_db (Path): File that contains the JSON
            """
        self.spaces_file = SpacesFile(spaces_file)
        self.wallpapers_db = WallpapersDB(wallpapers_db)

    @property
    def spaces(self):
        """Return the spaces from the spaces file."""
        return {space.uuid: space for space in self.spaces_file.spaces}

    @property
    def wallpapers(self):
        """Return the wallpapers from the wallpapers file."""
        return {wp.space_uuid: wp for wp in self.wallpapers_db.wallpapers}

    @property
    def uuids(self):
        """Return a list of all combined space UUIDs."""
        keys = set(chain(self.wallpapers.keys(), self.spaces.keys()))
        return list(keys)

    @property
    def images(self) -> dict:
        """Return a dictionary of desktop ID to image path."""
        spaces, walls = self.spaces, self.wallpapers

        images = {}
        for uuid in self.uuids:
            space = spaces[uuid]
            wp = walls[uuid]

            image = Image(space.number, space.uuid, wp.data_id, wp.image_path)
            images[space.number] = image

        images = dict(sorted(images.items(), key=lambda x: x[0]))

        return images

