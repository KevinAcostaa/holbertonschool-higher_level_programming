-- Listar todas las ciudades que contiene la data base hbtn_0d_usa
SELECT cities.id, cities.name, states.id
FROM cities
JOIN states ON state_id = states.id
ORDER BY cities.id ASC;