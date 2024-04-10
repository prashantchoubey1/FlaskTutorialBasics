-- SQLite
CREATE TABLE if not EXISTS details (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL
);

INSERT INTO details (id, name) VALUES (1, 'guddu');

SELECT * FROM details;