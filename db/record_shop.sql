DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS record_labels; 

CREATE TABLE record_labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    founded INT
); 

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    genre VARCHAR(255),
    record_label_id INT REFERENCES record_labels(id) ON DELETE CASCADE,
    stock INT,
    buy_price INT, 
    sell_price INT
); 



