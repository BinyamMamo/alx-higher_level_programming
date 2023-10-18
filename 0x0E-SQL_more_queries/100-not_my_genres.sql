-- List all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT
    name
FROM tv_genres
WHERE id NOT IN (
    SELECT 
        tsg.genre_id
    FROM tv_shows ts
    JOIN tv_show_genres tsg
        ON ts.id = tsg.show_id
    WHERE ts.title = 'Dexter'
)
ORDER BY name;