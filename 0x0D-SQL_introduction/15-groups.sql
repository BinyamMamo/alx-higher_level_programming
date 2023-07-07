-- displays the occurence a score appeared --
SELECT score, COUNT(*) AS "number" FROM second_table GROUP BY score DESC;
