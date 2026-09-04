-- 1. Alex treba da istraži koji žanrovi donose najveću zaradu i prikaže tri najisplativija žanra.

USE movies;

SELECT g.genre_id, g.name, SUM(m.box_office) as total_genre_profit
FROM Movie m
JOIN Genre g ON m.genre_id = g.genre_id
GROUP BY g.genre_id, g.name
ORDER BY total_genre_profit DESC
LIMIT 3;

-- Resenje: Action, Adventure, Sci-fi = 2320000000
--	    Action, Adventure, Superhero = 1910000000
--	    Animation, Adventure = 1844000000

-- 2. Koristeći SQL, izračunajte prosečan budžet i prosečnu zaradu po filmu.

USE movies;
SELECT AVG(budget) as average_budget, AVG(box_office) as average_box_office FROM Movie;

-- Resenje: average_budget = 159500000.0000, average_box_office = 1267000000.0000


-- 3. Izračunajte prosečnu zaradu po filmu za svaku zemlju i prikažite top 5 zemalja sa najvećim prosekom. 

USE movies;

SELECT c.country_id, c.country_name, AVG(m.box_office) as average_profit
FROM Movie m
JOIN Country c ON m.country_id = c.country_id
GROUP BY c.country_id, c.country_name
LIMIT 5;

-- Rešenje: United States of America = 1351444444.4444
--	    Japan = 507000000.0000


-- 4. Prikazati top 10 filmova po zaradi koristeći SQL upit.

USE movies;

SELECT title, box_office FROM movie
ORDER BY box_office DESC
LIMIT 10;



