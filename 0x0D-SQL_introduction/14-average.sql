-- computes the average of all records --
ALTER TABLE second_table ADD average INT;
UPDATE second_table SET average = AVG(score) *;
