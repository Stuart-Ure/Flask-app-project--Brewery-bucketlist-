DROP TABLE cities;
DROP TABLE breweries;


CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)    
    -- not null
);
CREATE TABLE breweries (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    city_id INTEGER,
    visited BOOLEAN NOT NULL DEFAULT FALSE
);
