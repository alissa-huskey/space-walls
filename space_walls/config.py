"""."""

from .object import Object
from .file import File


class Config(Object):
    """Stores the system configuration related to wallpapers."""

    def __init__(self, spaces_file = None, wallpapers_file = None):
        self.spaces_file = File(spaces_file)
        self.wallpapers_file = File(wallpapers_file)
