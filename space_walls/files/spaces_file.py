"""A spaces Plist file."""

from pathlib import Path

from space_walls.files.plist_file import PlistFile

class SpacesFile(PlistFile):
    """The logic specific to the spaces.json file."""

    PLIST_FILE = Path.home() / "Library" / "Preferences" / "com.apple.spaces.plist"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.path = self.path or self.PLIST_FILE

    @property
    def spaces(self):
        """Extract just the list of Spaces from the plist data."""
        if not self.data:
            return

        monitors = self.data.get("SpacesDisplayConfiguration", {}) \
            .get("Management Data", {}) \
            .get("Monitors", {})

        try:
            monitor = monitors[0]
        except IndexError:
            monitor = {}

        spaces = monitor.get("Spaces", {})

        return spaces


