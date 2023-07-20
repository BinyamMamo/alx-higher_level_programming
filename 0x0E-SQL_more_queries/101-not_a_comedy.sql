-- List all shows with a score greater or equal to 8.5 in the database hbtn_0d_tvshows
SELECT 
    title
FROM tv_shows
WHERE id NOT IN (
    SELECT 
        tsg.show_id
    FROM tv_show_genres tsg
    JOIN tv_genres tg
        ON tsg.genre_id = tg.id
    WHERE tg.name != 'Comedy'
);