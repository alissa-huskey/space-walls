from collections import namedtuple
from pathlib import Path

from space_walls.files.db import DB

Wallpaper = namedtuple("Wallpaper", ("data_id", "space_uuid", "image_path"))


class WallpapersDB(DB):
    """The sqlite desktoppicture.db"""

    DB_FILE = Path.home() / "Library" / "Application Support" / "Dock" / "desktoppicture.db"

    QUERY = """
        SELECT data.rowid, space_uuid as space, value as wallpaper
        FROM preferences
        JOIN data ON (data_id = data.rowid)
        JOIN pictures ON (preferences.picture_id = pictures.rowid)
        JOIN spaces ON (pictures.space_id = spaces.rowid)
        WHERE
        key = 1
        -- AND space_uuid != ""
        AND display_id = 1
        ORDER BY space
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.path = self.path or self.DB_FILE

    @property
    def wallpapers(self):
        """Return a list of wallpapers from the database."""
        data = self.select(self.QUERY)
        wallpapers = [Wallpaper(*row) for row in data]
        return wallpapers
