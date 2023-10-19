-- This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT
  g.genre AS genre,
  COUNT(sg.show_id) AS number_of_shows
FROM genres g
LEFT JOIN show_genres sg ON g.id = sg.genre_id
GROUP BY g.genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
