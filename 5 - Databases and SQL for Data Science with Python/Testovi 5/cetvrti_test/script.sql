-- 1. Pronaći sve filmove čiji je budžet veći od prosečnog budžeta svih filmova.

USE `movies`;
SELECT title, budget
FROM movie
WHERE budget > (
	SELECT AVG(budget)
    FROM movie
    );


-- 2. Za svaku državu, prikazati broj filmova.

USE `movies`;
SELECT c.country_name, COUNT(*) as total_movies
FROM Movie m
JOIN Country c ON m.country_id = c.country_Id
GROUP BY c.country_id;


-- 3. Prikazati žanrove koji imaju više od pet filmova u bazi.

USE `movies`;
SELECT g.genre_id, g.name, COUNT(*) as total_movies
FROM Movie m
JOIN Genre g ON m.genre_id = g.genre_id
GROUP BY g.genre_id
HAVING total_movies > 5;


-- 4. Prikazati top 10 filmova sa najvećom zaradom.

USE `movies`;
SELECT title, box_office
FROM movie
ORDER BY box_office DESC 
LIMIT 10;


-- 5. Prikazati pet filmova koji najkraće traju.

USE `movies`;
SELECT title, duration
FROM movie
ORDER BY duration ASC
LIMIT 5;


-- 6. Izračunati ukupnu zaradu svih filmova u bazi.

USE `movies`;
SELECT SUM(box_office) AS total_profit
FROM movie;


-- 7. Prikazati prosečno trajanje svih filmova.

USE `movies`;
SELECT AVG(duration) AS avg_duration
FROM movie;


-- 8. Pronaći najskuplji i najjeftiniji film po budžetu.

USE `movies`;
SELECT title, budget
FROM movie
WHERE budget = (
	SELECT MAX(budget)
    FROM movie
    )
UNION
SELECT title, budget
FROM movie
WHERE budget = (
	SELECT MIN(budget)
    FROM movie
    );


-- 9. Prikazati filmove gde naziv sadrži više od 15 karaktera i prikazati ih velikim slovima.

USE `movies`;
SELECT UPPER(title) as uppercase_title FROM movie
WHERE LENGTH(title) > 15;


-- 10. Prikazati prvih pet karaktera iz naslova svih filmova.

USE `movies`;
SELECT LEFT(title, 5) as short_title
FROM movie;

-- ili

USE `movies`;
SELECT SUBSTRING(title, 1, 5) AS short_title
FROM movie;










