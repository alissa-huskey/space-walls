Javascript for Automation (JXA)
===============================

These are my notes on using JXA, a Javascript-based language in general and to change your wallpaper.

that can be used in place of AppleScript ruin with the mac program `osascript`.

There doesn's seem to be any way to accomplish what I want using this method, but here are my notes anyway.
[macos-wallpaper]: https://github.com/sindresorhus/macos-wallpaper/

Changing the Wallpaper
----------------------

* [macOS: Change wallpaper by CLI](https://www.davd.io/macos-change-wallpaper-by-cli/) -- demonstrates how to set the wallpaper of the current space (I think) via JXA.

This script be used to print or set the current wallpaper.

As of macOS Sonoma (14) it only operates on the wallpaper you are currently on.

```javascript
#!/usr/bin/osascript -l JavaScript

var system = Application('System Events');
system.includeStandardAdditions = true

for (desktopIndex in system.desktops) {
  img = system.desktops[desktopIndex].picture()

  // print the current image
  console.log(img)


  // set it to a new image
  system.desktops[desktopIndex].picture = '/some/path/wallpaper.png';
}

// vim: ft=javascript
```

Using JXA
---------

* [JavaScript for Automation Cookbook](https://github.com/JXA-Cookbook/JXA-Cookbook/wiki/)
* [How to use JavaScript to control MacOS](https://til.codeinthehole.com/posts/how-to-use-javascript-to-control-macos/): General information on `JXA`
* [EvanLovely/get_title_and_url.applescript](https://gist.github.com/EvanLovely/cb01eafb0d61515c835ecd56f6ac199a): examples in both AppleScript and JXA of how to get the window title of all active browser tabs.
* [Scripting macOS with Javascript Automation](https://mikebian.co/scripting-macos-with-javascript-automation/)
* [JavaScript for Automation (JXA) Discussion](https://wiki.keyboardmaestro.com/JavaScript_for_Automation)
* [Scripting with JXA](https://bru6.de/jxa/)

See my example script [../bin/example.jxa]() for more info.

### osascript

JXA scripts are run via `osascript`.

An interactive console can be run like this:

```bash
osascript -il JavaScript
```

A simple command can be run like this:

```bash
osascript -l JavaScript -e 'console.log("hello")'
```

Or a script can be run like this:

```bash
osascript -l JavaScript myscript.jxa
```

Note: `console.log()` prints to stderr, so if yo want to pipe output to something you'll need to redirect output to stdout.

```bash
osascript -l JavaScript myscript.jxa 2>&1 | less
```

To create a script that can be run as an executable, the shabang line is:

```bash
#!/usr/bin/osascript -l JavaScript

console.log("Hello World")
```

### Sample

Here is a sample script that contains a bunch of random information.

```javascript
#!/usr/bin/osascript -l JavaScript

ObjC.import('stdlib')
ObjC.import('AppKit')

console.log(Object.getOwnPropertyNames(this).join('\n'))

var app = Application.currentApplication()
app.includeStandardAdditions = true

// Note these never take () unless they have arguments
var apps = $.NSWorkspace.sharedWorkspace.runningApplications

// Unwrap the NSArray instance to a normal JS array
apps = ObjC.unwrap(apps)

```


AppKit
------

* [AppKit Docs](https://developer.apple.com/documentation/appkit)
* [AppKit Docs > NSWorkspace](https://developer.apple.com/documentation/appkit/nsworkspace)
* [AppleScript Language Guide](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
* [Setting Wallpaper from the Command Line in Mac OS X](https://osxdaily.com/2015/08/28/set-wallpaper-command-line-macosx/): describes how to change the (current?) wallpaper via AppleScript.
* [sindresorhus/macos-wallpaper > Wallpaper.swift](https://github.com/sindresorhus/macos-wallpaper/blob/main/Sources/wallpaper/Wallpaper.swift#L96): a swift file from the [macos-wallpaper][] project. The `set` function changes the wallpaper for the current space (I think) via the  `NSWorkspace` object in `AppKit`.
* [Standard AppleScript Commands](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html)

JXA uses AppKit to manage desktop settings on the map in JXA, Swift and AppleScript. I've found that sometime scripts in AppleKit or Swift can help me understand how to access certain settings in JXA, though the way the objects are laid out does not seem to be one-to-one.


The closest to an API you can get is to open the Script Editor app and go to File -> Open Dictionary.

