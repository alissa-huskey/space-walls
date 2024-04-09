"""A spaces JSON file."""

from space_walls.files.json_file import JSONFile

class SpacesJSONFile(JSONFile):
    """The logic specific to the spaces.json file."""

    @property
    def spaces(self):
        if not self.data:
            return
        monitors = self.data.get("SpacesDisplayConfiguration", {}) \
            .get("Management Data", {}) \
            .get("Monitors", {})

        data = monitors[0].get("Spaces")
        spaces = {s["uuid"]: s for s in data}

        return spaces
