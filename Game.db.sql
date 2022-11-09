--
-- File generated with SQLiteStudio v3.3.3 on Tue Nov 8 19:10:55 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: business
CREATE TABLE business (b_name CHAR (20) NOT NULL, b_revenue INTEGER (20, 0) NOT NULL, b_key INTEGER (20, 0) NOT NULL, b_ceo CHAR (20) NOT NULL);
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('EA Sports', 6.99, 1, 'Andrew Wilson');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('2K Sports', 1.21, 2, 'Andrew Walker');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('Nintendo', 1695, 3, 'Satoru Iwata');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('Sony Interactive Entertainment', 2739, 4, 'Jim Ryan');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('Konami', 262.8, 5, 'Kagemasa Kozuki');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('Plaion', 0.042, 6, 'Klemens Kundratitz');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('Deep Silver', 0.02, 7, 'Maria Popo');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('BNE Entertainment', 240.3, 8, 'Naoki Katashima');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('FromSoftware', 0.835, 9, 'Hidetaka Miyazaki');
INSERT INTO business (b_name, b_revenue, b_key, b_ceo) VALUES ('Sega', 247.7, 10, 'Haruki Satomi');

-- Table: console
CREATE TABLE console (c_name CHAR (20) NOT NULL, c_id INTEGER (20, 0) NOT NULL, c_units INTEGER (20, 0) NOT NULL);
INSERT INTO console (c_name, c_id, c_units) VALUES ('Windows', 1, 184.47);
INSERT INTO console (c_name, c_id, c_units) VALUES ('PS4', 2, 117.2);
INSERT INTO console (c_name, c_id, c_units) VALUES ('PS5', 3, 25);
INSERT INTO console (c_name, c_id, c_units) VALUES ('XBOX ONE', 4, 54);
INSERT INTO console (c_name, c_id, c_units) VALUES ('XBOX ONE S', 5, 58.5);
INSERT INTO console (c_name, c_id, c_units) VALUES ('XBOX Series X', 6, 12);
INSERT INTO console (c_name, c_id, c_units) VALUES ('XBOX Series S', 7, 12);
INSERT INTO console (c_name, c_id, c_units) VALUES ('Nintendo Switch', 8, 114.33);
INSERT INTO console (c_name, c_id, c_units) VALUES ('Mac', 9, 48.6);
INSERT INTO console (c_name, c_id, c_units) VALUES ('Steam Deck', 10, 1);

-- Table: developer
CREATE TABLE developer (d_key INTEGER (20, 0) NOT NULL, d_name CHAR (20) NOT NULL, d_head CHAR (20) NOT NULL, d_employees INTEGER (20, 0) NOT NULL);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (1, 'Electronic Arts', 'Andrew Wilson', 8286);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (2, 'EA Tiburon', 'Andrew Wilson', 927);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (3, 'Visual Concepts', 'Scott Patterson', 350);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (4, 'Nintendo EPD', 'Satoru Iwata', 15827);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (5, 'Naughty Dog', 'Evan Wells', 2187);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (6, 'Digital Eclipse', 'Mike Mika', 639);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (7, 'Deep Silver Volition', 'Mike Kulas', 1976);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (8, 'CyberConnect2', 'Hiroshi Matsumaya', 285);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (9, 'FromSoftware', 'Hidetaka Miyazaki', 349);
INSERT INTO developer (d_key, d_name, d_head, d_employees) VALUES (10, 'Sonic Team', 'Haruki Satomi', 7235);

-- Table: Games 2022
CREATE TABLE "Games 2022" (g_name CHAR (20) NOT NULL, g_id INTEGER (20, 0) NOT NULL, g_prices INTEGER (20, 0) NOT NULL, g_sold INTEGER (20, 0) NOT NULL, g_date DATE NOT NULL, g_genre CHAR (20) NOT NULL, g_cid INTEGER (20, 0));
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('FIFA 23', 1, 60, 8.5, '26-09', 'Sport', 3);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('Madden NFL 23', 2, 60, 7.2, '19-08', 'Sport', 5);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('NBA 2K23', 3, 60, 46, '08-09', 'Sport', 3);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('Splatoon 3', 4, 60, 4.3, '08-09', 'Shooter', 8);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('The Last of Us: Part 1', 5, 60, 17, '02-09', 'Action', 3);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('Teenage Mutant Ninja Turtles: The Cowabunga Collection', 6, 60, 6.5, '30-08', 'Action', 4);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('Saints Row (2022)', 7, 60, 1.7, '23-08', 'Open World', 7);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('JoJo''s Bizarre Adventure: All Star Battle R', 8, 60, 13.6, '01-09', 'Fighting', 1);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('Elden Ring', 9, 60, 16.6, '25-02', 'Adventure', 1);
INSERT INTO "Games 2022" (g_name, g_id, g_prices, g_sold, g_date, g_genre, g_cid) VALUES ('Sonic Frontiers', 10, 60, 1, '08-11', 'Platform', 8);

-- Table: reviews
CREATE TABLE reviews (r_name CHAR (10) NOT NULL, r_score INTEGER (10, 0) NOT NULL, r_reviewers CHAR (10) NOT NULL, r_id INTEGER (10, 0) NOT NULL);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('FIFA 23', 7, 'IGN', 1);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('Madden NFL 23', 7, 'IGN', 2);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('NBA 2K23', 6, 'IGN', 3);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('Splatoon 3', 8, 'IGN', 4);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('The Last of Us: Part 1', 9, 'IGN', 5);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('Teenage Mutant Ninja Turtles: The Cowabunga Collection', 7, 'IGN', 6);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('Saint''s Row 2022', 6, 'IGN', 7);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('JoJo''s Bizarre Adventure: All Star Battle R', 7, 'IGN', 8);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('Elden Ring', 10, 'IGN', 9);
INSERT INTO reviews (r_name, r_score, r_reviewers, r_id) VALUES ('Sonic Frontiers', 7, 'IGN', 10);

-- Table: stores
CREATE TABLE stores (s_name CHAR (10) NOT NULL, s_discount INTEGER (10, 0) NOT NULL);
INSERT INTO stores (s_name, s_discount) VALUES ('Walmart', 'YES');
INSERT INTO stores (s_name, s_discount) VALUES ('Target', 'YES');
INSERT INTO stores (s_name, s_discount) VALUES ('BestBuy', 'NO');
INSERT INTO stores (s_name, s_discount) VALUES ('GameStop', 'YES');
INSERT INTO stores (s_name, s_discount) VALUES ('Steam', 'YES');
INSERT INTO stores (s_name, s_discount) VALUES ('BattleNet', 'YES');
INSERT INTO stores (s_name, s_discount) VALUES ('Epic', 'YES');
INSERT INTO stores (s_name, s_discount) VALUES ('Origin', 'NO');
INSERT INTO stores (s_name, s_discount) VALUES ('DKoldies', 'NO');
INSERT INTO stores (s_name, s_discount) VALUES ('NewEgg', 'NO');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
