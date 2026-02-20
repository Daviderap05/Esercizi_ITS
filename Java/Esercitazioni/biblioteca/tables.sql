-- Active: 1764194045216@@localhost@5432@mavenits
CREATE TABLE libro (
    id SERIAL PRIMARY KEY,
    titolo VARCHAR(255) NOT NULL,
    autore VARCHAR(255) NOT NULL,
    prezzo DECIMAL(10,2) NOT NULL
);