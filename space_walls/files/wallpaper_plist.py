"""A wallpaper Plist file.

Where macOS Sonoma+ stores wallpaper configuration.

Typically stored at:

    ~/Library/Application Support/com.apple.wallpaper/Store/Index.plist

Accessed at:

    ["Spaces"][SPACE_UUID][N]["Displays"][DISPLAY_UUID]["Desktop"]["Content"]["Choices"][N][DISPLAY_UUID]["Files"][0]["relative"]

See also:

    ["Spaces"][SPACE_UUID][N]["Default"]["Content"]
"""

from collections import defaultdict
from pathlib import Path

from space_walls.files.plist_file import PlistFile


class WallpaperPlist(PlistFile):
    """Wallpaper Plist File class."""

    PLIST_FILE = Path.home() / "Library" / "Application Support" / "com.apple.wallpaper" / "Store" / "Index.plist"

    @property
    def displays(self):
        """List of display uuids."""
        spaces = self.data["Spaces"].values()
        ids = set([v for s in spaces for v in s["Displays"]])
        return list(ids)

    @property
    def files(self):
        """Return a dict of {display uuid: {space uuid: wallpaper file}}."""
        res = defaultdict(dict)
        for suuid, space in self.data["Spaces"].items():
            for duuid, display in space["Displays"].items():
                choices = display["Desktop"]["Content"]["Choices"]
                files = [x["Files"] for x in choices]
                # don't know why these are lists
                file = files[0][0]
                if "relative" not in file:
                    continue
                res[duuid][suuid] = file["relative"]
        return res
