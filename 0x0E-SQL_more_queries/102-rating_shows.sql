-- comment here
SELECT 
    title, 
    SUM(rate) AS rating
FROM tv_shows AS ts
    INNER JOIN tv_show_ratings AS tsr
    ON t.id = r.show_id
GROUP BY title
ORDER BY rating DESC;