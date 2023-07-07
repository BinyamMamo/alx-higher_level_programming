-- computes the average of all records --
ALTER TABLE first_table ADD average INT;
UPDATE first_table SET average = AVG(score);
