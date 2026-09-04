USE movies;

INSERT INTO director (firstname, lastname) 
VALUES 
    ('James', 'Cameron'),
    ('Jon', 'Watts'),
    ('Greta', 'Gerwig'),
    ('Joseph', 'Kosinski'),
    ('Aaron', 'Horvath'),
    ('Chris', 'Buck'),
    ('Kyle', 'Balda'),
    ('Haruo', 'Sotozaki'),
    ('Matt', 'Reeves'),
    ('Joel', 'Crawford')


INSERT INTO genre (name) 
VALUES 
    ('Action, Adventure, Sci-fi'),
    ('Action, Adventure, Superhero'),
    ('Comedy, Fantasy'),
    ('Action, Drama'),
    ('Animation, Adventure'),
    ('Animation, Fantasy'),
    ('Animation, Comedy'),
    ('Animation Action'),
    ('Drama, History'),
    ('Sci-Fi, Action')


INSERT INTO country (country_name) 
VALUES 
    ('USA'),
    ('UK'),
    ('Japan'),
    ('Sweden'),
    ('South Korea'),
    ('Ireland'),
    ('Australia'),
    ('France'),
    ('Russia'),
    ('Germany')


INSERT INTO language (language_name) 
VALUES 
    ('English'),
    ('Japanese'),
    ('Korean'),
    ('Swedish'),
    ('Irish'),
    ('Australian'),
    ('French'),
    ('Russian'),
    ('German'),
    ('Spanish')


INSERT INTO movie (title, year, duration, budget, box_office, genre_id, director_id, language_id, country_id) 
VALUES 
    ('Avatar: The Way of Water', '2022', '192', '460000000', '2320000000', '1', '1', '1', '1'),
    ('Spider-Man: No Way Home', '2021', '148', '200000000', '1910000000', '2', '2', '1', '1'),
    ('Barbie', '2023', '114', '145000000', '1440000000', '3', '3', '1', '1'),
    ('Top Gun: Maverick', '2022', '130', '170000000', '1490000000', '4', '4', '1', '1'),
    ('The Super Mario Bros. Movie', '2023', '92', '100000000', '1360000000', '5', '5', '1', '1'),
    ('Frozen II', '2019', '103', '150000000', '1450000000', '6', '6', '1', '1'),
    ('Minions: The Rise of Gru', '2022', '87', '80000000', '939000000', '7', '7', '1', '1'),
    ('Demon Slayer: Kimetsu no Yaiba - The Movie: Mugen Train', '2020', '117', '15000000', '507000000', '8', '8', '2', '3'),
	('The Batman', '2022', '176', '185000000', '770000000', '9', '9', '1', '1'),
    ('Puss in Boots: The Last Wish', '2022', '102', '90000000', '484000000', '5', '10', '1', '1')


UPDATE country SET country_name = 'United States of America' WHERE country_id = 1
UPDATE country SET country_name = 'United Kingdom' WHERE country_id = 2

-- U mojoj tabeli nema filmova sa trajanjem manjim od 70 minuta
DELETE FROM movie WHERE duration < 70


SELECT title, duration, budget 
FROM movie WHERE duration BETWEEN 120 AND 150 AND budget > 200000 ORDER BY duration