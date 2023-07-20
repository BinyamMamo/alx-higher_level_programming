-- comment here
SELECT 
    ts.title 'name',
    (SELECT 
        SUM(tsr.rate)
    FROM tv_show_ratings tsr
    WHERE tsr.show_id = ts.id
    ) AS 'ratings'
FROM tv_shows ts
ORDER BY ratings DESC;