This folder contains files that support the program.

* [query.sql](query.sql): The query to run on the sqlite3 `desktoppicture.db`
  database to produce a list of spaces and wallpapers.
* [wallpapers.json](wallpapers.json): Produced by sqlite3 using the above query.
* [spaces.json](spaces.json): The `com.apple.spaces` plist file converted to
  JSON by `plutil`.
