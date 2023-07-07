-- displays the occurence a score appeared --
SELECT score, COUNT(*) AS "number" GROUP BY score DESC FROM second_table;
