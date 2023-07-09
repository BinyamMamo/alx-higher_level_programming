-- imports data dump --
SELECT `city`, AVG(`city`) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
