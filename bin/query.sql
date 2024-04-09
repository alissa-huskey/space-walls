--
-- This SQL query should be run against the sqlite3 database:
-- ~/Library/Application Support/Dock/desktoppicture.db
-- 
-- It will return the data.rowid, space_uuid and path to the wallpaper picture
-- 
--

-- This query will give you the results for display 1

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

-- This query will give you the results for all displays

--  SELECT display_id as display, space_uuid as space, value as wallpaper
--  FROM preferences
--  JOIN data ON (data_id = data.rowid)
--  JOIN pictures ON (preferences.picture_id = pictures.rowid)
--  JOIN spaces ON (pictures.space_id = spaces.rowid)
--  WHERE
--    key = 1
--    AND space_id IS NOT NULL
--    and space_uuid != ""
--  ORDER BY display, space
