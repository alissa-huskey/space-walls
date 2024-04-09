"""A Wallpapers JSON file."""

from space_walls.files.json_file import JSONFile

class WallpapersFile(JSONFile):
    """The logic specific to the wallpapers.json file."""

    @property
    def wallpapers(self):
        wallpapers = {w["space"]: w for w in self.data}
        return wallpapers






