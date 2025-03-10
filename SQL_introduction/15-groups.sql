-- Enumerar la cantidad de registro con la misma puntuacion en una tabla
SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;