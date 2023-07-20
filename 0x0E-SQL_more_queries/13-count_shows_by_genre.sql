-- List genres with number of shows using JOIN statement
SELECT
    name AS 'genre',
    (SELECT COUNT(genre_id) FROM tv_show_genres WHERE tv_genres.id = genre_id) AS 'number_of_shows'
FROM tv_genres
ORDER BY number_of_shows DESC;
