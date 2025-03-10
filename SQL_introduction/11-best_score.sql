-- listar todos los registro con puntuacion >= 10 en una table
SELECT score, name
FROM second_table
WHERE score >= 10 
ORDER BY score DESC;