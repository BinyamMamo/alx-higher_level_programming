-- List genres with number of shows using JOIN statement
SELECT 
    tg.name AS 'genre',
    COUNT(tg.name) AS 'number_of_shows'
FROM tv_genres tg
JOIN tv_show_genres tsg
    ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
