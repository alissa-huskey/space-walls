System Images
=============

System images are stored here:

`/Library/Caches/Desktop Pictures/{uid}/lockscreen.png`

This will give you a list of all pictures (though not the path).

`plutil -p /System/Library/Desktop\ Pictures/.orderedPictures.plist | less`

They may also be stored in one of the following:

`~/Library/Application Support/com.apple.mobileAssetDesktop/`
`/System/Library/Desktop Pictures`

### Default Desktop Picture

The default desktop pictures are stored here. However, it cannot be easily
changed due to readonly FS.

```
/System/Library/CoreServices/DefaultBackground.jpg
/System/Library/CoreServices/DefaultDesktop.heic
```
