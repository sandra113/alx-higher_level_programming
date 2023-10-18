-- this script lists all the cities of California

-- Find the state_id for California
SELECT id FROM states WHERE name = 'California'

-- List all the cities in California
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
