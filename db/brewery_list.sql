DROP TABLE breweries;
DROP TABLE cities;


CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)    
    -- not null
);
CREATE TABLE breweries (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    city_id INT REFERENCES cities ON DELETE CASCADE, 
    visited BOOLEAN NOT NULL DEFAULT FALSE
);
