"""A Wallpapers JSON file."""

from space_walls.file import File
from .attr import attr

class WallpapersFile(File):
    """The logic specific to the wallpapers.json file."""

    @property
    def wallpapers(self):
        wallpapers = {w["space"]: w for w in self.data}
        return wallpapers






