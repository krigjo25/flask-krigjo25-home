CREATE TABLE github (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    gurl TEXT NOT NULL,
    yurl TEXT NOT NULL,
    date DATETIME);

CREATE TABLE education IF NOT EXISTS (
    id INTEGER AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    curl TEXT NOT NULL DEFAULT false,
);

CREATE TABLE cookies IF NOT EXISTS (
    id INTEGER AUTOINCREMENT NOT NULL,
    txtfile BLOB NOT NULL,
    dd TIMESTAMP NOT NULL,
)