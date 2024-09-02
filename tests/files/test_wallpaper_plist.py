from space_walls.files.wallpaper_plist import WallpaperPlist


def test_wallpaper_plist():
    file = WallpaperPlist()
    assert file


def test_wallpaper_plist_files(fixture_file):
    path = fixture_file("com.apple.wallpaper.plist")
    file = WallpaperPlist(path)
    displays = file.files

    assert isinstance(displays, dict)
    assert len(displays) == 1

    # get the first display
    display = list(displays.values())[0]

    assert len(display) == 12
    assert display[""] == "file:///Users/alissa/Pictures/photos/blue-bubbles-by-cynthiathomas.jpg"
