-- Active: 1764194045216@@localhost@5432@area_verde
CREATE DOMAIN realLat as REAL
    CHECK (VALUE BETWEEN -90 AND 90);

CREATE DOMAIN realLong as REAL
    CHECK (VALUE BETWEEN -180 AND 180);

CREATE DOMAIN intDurata as INTEGER
    CHECK (VALUE > 0);

CREATE DOMAIN intPriorità as INTEGER
    CHECK (VALUE BETWEEN 1 AND 10);

CREATE DOMAIN CF as CHAR(16);


CREATE TABLE Specie (
    n_scientifico VARCHAR(200) PRIMARY KEY,
    n_comune VARCHAR(200) NOT NULL
);

CREATE TABLE AreaVerde (
    id SERIAL PRIMARY KEY,
    latitudine realLat NOT NULL,
    longitudine realLong NOT NULL,
    is_fruibile BOOLEAN NOT NULL,
    is_sensibile BOOLEAN,

    check (NOT is_sensibile or is_fruibile) -- "se A allora B"
);

CREATE TABLE SoggettoVerde (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    -- accorpo Specie
    specie VARCHAR(200) NOT NULL,
    Foreign Key (specie) 
        REFERENCES Specie(n_scientifico),
    -- accorpo AreaVerde
    areaVerde INTEGER NOT NULL,
    Foreign Key (areaVerde) 
        REFERENCES AreaVerde(id)
);

CREATE TABLE Intervento (
    id SERIAL PRIMARY KEY,
    inizio TIMESTAMP NOT NULL,
    durata intDurata NOT NULL,
    priorità intPriorità NOT NULL,
    -- accorpo AreaVerde
    areaVerde INTEGER NOT NULL,
    Foreign Key (areaVerde) 
        REFERENCES AreaVerde(id)
);

CREATE TABLE InterventoAssegnato (
    fine TIMESTAMP,
    --accorpo Intervento
    intervento INTEGER NOT NULL,
    Foreign Key (intervento) 
        REFERENCES Intervento(id),

    PRIMARY KEY (intervento)
    --v.incl (intervento) 
    --  occorre in Assegna(InterventoAssegnato)
);

CREATE TABLE Operatore (
    cf CF PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    cognome VARCHAR(200) NOT NULL,
    inizio DATE NOT NULL,
    fine DATE
);

CREATE TABLE Assegna (
    interventoAssegnato INTEGER NOT NULL,
    operatore CF NOT NULL,
    istante TIMESTAMP NOT NULL,

    Foreign Key (interventoAssegnato) 
        REFERENCES InterventoAssegnato(intervento),
    Foreign Key (operatore)     
        REFERENCES Operatore(cf),

    PRIMARY KEY (interventoAssegnato, operatore)
);