Spaces plist
============

Information about your spaces is stored in the `plist` file:

`~/Library/Preferences/com.apple.spaces.plist`

To read it use the `plutil` program.

```bash
plutil -p ~/Library/Preferences/com.apple.spaces.plist
```

You can convert the output of a `plist` file to `json`:

```bash
plutil -convert json -o spaces.json ~/Library/Preferences/com.apple.spaces.plist
```

Then use your preferred method of handling `JSON` files.

I'm fond of [jq](https://github.com/jqlang/jq), a command-line JSON parser.

```bash
jq '.SpacesDisplayConfiguration["Management Data"]["Monitors"][0]["Spaces"]' spaces.json
```
