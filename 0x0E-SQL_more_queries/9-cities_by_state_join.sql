-- join selection
-- sub queries
SELECT cities.id, cities.name, (SELECT name FROM states WHERE states.id = cities.state_id) as name
FROM cities
ORDER BY cities.id ASC;
