System Images
=============

System images may be stored in the following locations:

`/Library/Caches/Desktop Pictures/{uid}/lockscreen.png`
`/System/Library/Desktop Pictures`
`~/Library/Application Support/com.apple.mobileAssetDesktop/`

This may give you a list of all (built-in?) pictures.

`plutil -p /System/Library/Desktop\ Pictures/.orderedPictures.plist | less`

### Default Desktop Picture

The default desktop pictures are stored here. However, it cannot be easily
changed due to readonly FS.

```
/System/Library/CoreServices/DefaultBackground.jpg
/System/Library/CoreServices/DefaultDesktop.heic
```
