-- displays the occurence a score appeared --
SELECT score, COUNT(score) AS "number" GROUP BY score ORDER BY score DESC FROM second_table;
