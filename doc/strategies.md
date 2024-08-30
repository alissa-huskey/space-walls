Desktop Settings Strategies
===========================

The ways that macOS has stored wallpaper settings in different versions.

Versions
--------

* [macos-desktop](https://github.com/tech-otaku/macos-desktop/tree/main) -- works on 13-10.14. Also includes information on macOS 10.14-13.
* [A Comparison of Apple-supplied Desktop Images Since macOS 10.14 Mojave](https://desktop.tech-otaku.com/)

| Version | Name          | Released   | System |
|---------|---------------|------------|--------|
| 15      | Sequoia       | 2024, Fall | A      |
| 14      | Sonoma        | 2023-09-26 |        |
| 13      | Ventura       | 2022-10-25 |        |
| 12      | Monterey      | 2021-10-25 | B      |
| 11      | Big Sur       | 2020-11-19 |        |
| 10.15   | Catalina      | 2019-10-07 |        |
| 10.14   | Mojave        | 2018-08-24 |        |
| 10.13   | High Sierra   | 2017-09-25 |        |
| 10.12   | Sierra        | 2016-09-20 |        |
| 10.11   | El Capitan    | 2015-09-30 |        |
| 10.10   | Yosemite      | 2014-10-16 | B      |
| 10.9    | Mavericks     | 2013-10-22 | C      |
| 10.8    | Mountain Lion | 2012-07-25 | B?     |
| 10.7    | Lion          | 2011-07-20 | C      |
| 10.6    | Snow Leopard  | 2009-08-28 |        |
| 10.5    | Leopard       | 2007-10-26 |        |
| 10.4    | Tiger         | 2005-04-29 |        |
| 10.3    | Panther       | 2003-10-24 |        |
| 10.2    | Jaguar        | 2002-08-23 |        |
| 10.1    | Puma          | 2001-09-25 |        |
| 10.0    | Cheetah       | 2001-03-24 |        |

* [**A**]: com.apple.wallpaper
* [**B**]: desktoppicture.db
* [**C**]: com.apple.desktop


A. com.apple.wallpaper
----------------------

* [MacOS Sonoma Screen Saver Configuration plist](https://github.com/JohnCoates/Aerial/issues/1332) -- github issue discussing screensaver config, which seems to be in the same place.

```bash
plutil -p ~/Library/Application\ Support/com.apple.wallpaper/Store/Index.plist
```

B. desktoppicture.db
--------------------

See [](wallpapers-database.md).

In this system, some sources say you can also use AppleScript as such.

```bash
osascript -e 'tell app "finder" to get posix path of (get desktop picture as alias)'
```

C. com.apple.desktop
--------------------

* [Getting desktop background on Mac](https://stackoverflow.com/questions/301215/getting-desktop-background-on-mac/301573#301573)
* [Setting the Desktop Image in macOS Mojave From the Command Line](https://www.tech-otaku.com/mac/setting-desktop-image-macos-mojave-from-command-line/)

`~/Library/Preferences/com.apple.desktop.plist`

Key `default` > `ImageFilePath`.

```bash
defaults write com.apple.desktop Background '{default = {ImageFilePath = "/path/to/desktop/image.jpg";};}'
```

Misc
----

In old versions, display info may have been kept at:

`~/Desktop/com.apple.windowserver.displays.plist`

Others
------

* [AppKit Docs](https://developer.apple.com/documentation/appkit/nsworkspace#//apple_ref/occ/instm/NSWorkspace/desktopImageURLForScreen) -- docs for NSWorkspace.desktopImageURLForScreen.
* [whichbg](https://github.com/musically-ut/whichbg) -- Swift/Cocoa app written in 2015.
* [How to get macOS wallpaper image URL which respects the current color scheme?](https://stackoverflow.com/questions/78452829/how-to-get-macos-wallpaper-image-url-which-respects-the-current-color-scheme) -- Swift code referencing `NSWorkspace.shared.desktopImageURL` that allegedly works on Sonoma. 
* [Get the current wallpaper in Cocoa](https://stackoverflow.com/questions/14099363/get-the-current-wallpaper-in-cocoa) --  more Swift code from 2014.
* [desktoppr](https://github.com/scriptingosx/desktoppr) -- Swift app that works on Sonoma for the current desktop only.
* [wallget.py](https://github.com/mikeswanson/WallGet/blob/main/wallget.py) -- allegedly works on Sonoma.
* [Managing the “Click wallpaper to reveal desktop” setting in macOS Sonoma](https://derflounder.wordpress.com/2023/09/26/managing-the-click-wallpaper-to-reveal-desktop-setting-in-macos-sonoma/)
* [macos-wallpaper](https://github.com/sindresorhus/macos-wallpaper) --Swift app for 10.14.4 "or later".
* [wallpaper](https://github.com/sindresorhus/wallpaper) -- javascript app for 10.14.4+.
* [macOS Sonoma or later: APPLY YOUR OWN DYNAMIC WALLPAPER! A tutorial](https://www.reddit.com/r/MacOS/comments/1eqbq37/macos_sonoma_or_later_apply_your_own_dynamic/)
