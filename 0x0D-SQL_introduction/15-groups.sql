-- lists the numbers of records with the same score
-- List should be sorted by number of records in descending order
-- Number of records for the score should be labelled as number
SELECT score, COUNT(*) AS 'number'
FROM second_table
GROUP BY score
ORDER BY 'number' DESC;
