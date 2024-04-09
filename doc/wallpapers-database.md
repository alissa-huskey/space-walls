
Wallpapers Database
===================

* [Setting the Desktop Image in macOS Mojave from the Command Line](https://www.tech-otaku.com/mac/setting-desktop-image-macos-mojave-from-command-line/)
* [How do I change desktop background with a terminal command?](https://apple.stackexchange.com/questions/40644/how-do-i-change-desktop-background-with-a-terminal-command)
* [pywal > wallpaper.py](https://github.com/dylanaraps/pywal/blob/master/pywal/wallpaper.py#L91)

The sqlite database containing all the relevant preferences is here:

`~/Library/Application Support/Dock/desktoppicture.db`

Schema
------

The database schema is not at all intuitive. To follow is what I have come to
understand after a great deal of sleuthing.

The following diagram is a very simplified representation of the connections
involved in getting to the wallpaper information.

[![][diagram-img]][diagram-url]

[diagram-img]: https://mermaid.ink/img/pako:eNplz0tqwzAQBuCrDLNyIM4BDOkqPUGzCoIwSGNHYD3QI6WE3L0jO84mK_0jffqRHqiDYRxwnMOvvlEqcD4pDzHxyIm95gzHI0SrS018tUamr23MDb5iUzmSfptlyJ9VhgptpmURbYG-hzvNlSUEsG7qOuto4t1OwNrVyJqutUpDgzl23bK3OLkG_eHQGO7RcXJkjXzuIWegsNzYscJBouGR6lwUKv8UWqO8gb-NLSHhMNKceY9US_j58xqHkipv6GRpSuTeKpK_hOBW9PwH60lxwg?type=png
[diagram-url]: https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNplz0tqwzAQBuCrDLNyIM4BDOkqPUGzCoIwSGNHYD3QI6WE3L0jO84mK_0jffqRHqiDYRxwnMOvvlEqcD4pDzHxyIm95gzHI0SrS018tUamr23MDb5iUzmSfptlyJ9VhgptpmURbYG-hzvNlSUEsG7qOuto4t1OwNrVyJqutUpDgzl23bK3OLkG_eHQGO7RcXJkjXzuIWegsNzYscJBouGR6lwUKv8UWqO8gb-NLSHhMNKceY9US_j58xqHkipv6GRpSuTeKpK_hOBW9PwH60lxwg

What follows is a detailed explanation of each table in the schema and their respective columns.

### preferences

* rowid      - primary key
* picture_id - pictures.rowid
* key        - number indicating what kind of value is stored in the data field
* data_id    - data.rowid

### data

* rowid - primary id
* value

### pictures

* rowid      - primary key
* space_id   - spaces.rowid
* display_id - displays.rowid

### spaces

* rowid      - desktop number
* space_uuid - uuid as found in com.apple.spaces

### displays

* rowid        -  primary key
* display_uuid -

Decoding Preferences
--------------------

Each row of the `preferences` table contains a number in the `preferences.key`
column that indicates what kind of setting it points to. That row is linked to
the `data` table via `preferences.data_id = data.rowid`. The user's saved
configuration for that row is stored in the `data` table at `data.value`
column.

The table below is a key to the `preferences.key` numbers, as well as the
kind information that is expected for each in `data.value`.


| preferences.key | meaning                | data.value                                   |
|-----------------|------------------------|----------------------------------------------|
| 1               | image file             | path to the image                            |
| 2               | arrangement on desktop | 2-5 for tile/center/stretch/fit (see below)  |
| 3, 4, 5         | RGB values [^1]        | a red, green or blue number (probably 0-255) |
| 10              | image directory [^2]   | path to directory that contains the image    |
| 20              | dynamic selection      | 0-4 for auto/dynamic/light/dark (see below)  |

[^1]: For centered/fit to screen images. (The background color I guess?)
[^2]: Used for non-system images.

It's worth noting that most of these options have disappeared in the System
Settings app as of macOS Sonoma (14.4.1). I have no idea if they will have any
effect or if they are obsolete.

### picture orientation options

- 2: tile
- 3: center
- 4: stretch to fill screen
- 5: fit to screen

### dynamic selection options

- 0: Automatic (Light and Dark Desktops)
- 1: Dynamic (Dynamic Desktops)
- 2: Light (Still)
- 3: Dark (Still)

Query
-----

The following query will extract which wallpapers are on each desktop (space).

(If you have more than one display you'll need to modify the SQL a bit. See the
`query.sql` file for more info, but for the time being I'm only going to worry
about display `1`.)

```sql
SELECT data.rowid, space_uuid as space, value as wallpaper
FROM preferences 
JOIN data ON (data_id = data.rowid) 
JOIN pictures ON (preferences.picture_id = pictures.rowid)
JOIN spaces ON (pictures.space_id = spaces.rowid)
WHERE
  key = 1
  AND space_id IS NOT NULL
  AND space_uuid != ""
  AND display_id = 1
ORDER BY space
```

Download the [query.sql](assets/query.sql), then run the following command to
save to store the data in the file `wallpapers.json`.

```bash
db=~/Library/Application\ Support/Dock/desktoppicture.db
sqlite3 -noheader -json "$db" < query.sql > wallpapers.json
```

## Recreating the database

You can recreate the database with:

```bash
# this might be "System Settings" now, not sure

killall "System Preferences" > /dev/null 2>&1 \
    && rm ~/Library/Application\ Support/Dock/desktoppicture.db \
    && killall Dock
```

I guess you might need to do this if you messed it up badly. I'd recommend
backing it up (just make a copy somewhere else) before making any changes.
