-- Enumerar todas las ciudades de California que se encuentren en la base de datos hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;