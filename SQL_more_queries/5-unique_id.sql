-- Create table unique_id with DEFAULT VALUE and UNIQUE
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);