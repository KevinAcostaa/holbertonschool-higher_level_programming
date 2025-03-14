--
SELECT tg.name AS genre,
COUNT(ts.show_id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_show_genres ts ON tg.id = ts.genre_id
GROUP BY tg.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;