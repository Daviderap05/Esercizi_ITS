-- Active: 1764194045216@@localhost@5432@rocklog
create domain intgz as Integer
    check (value > 0);

create domain intgez as Integer
    check (value >= 0);

create domain Lat as Real
    check (value BETWEEN -90 AND +90);

create domain Log as Real
    check (value BETWEEN -180 AND +180);

create type Coordinate as Enum ('N', 'S', 'W', 'E');




CREATE TABLE Persona (
    username VARCHAR PRIMARY KEY
);


CREATE TABLE Arrampicatore (
    nome VARCHAR,
    cognome VARCHAR,

    persona VARCHAR NOT NULL,
    Foreign Key (persona) 
        REFERENCES Persona(username),

    PRIMARY KEY (persona)
);


CREATE TABLE Chiodatore (
    persona VARCHAR NOT NULL,
    Foreign Key (persona) 
        REFERENCES Persona(username),

    PRIMARY KEY (persona)
);


CREATE TABLE falesia (
    nome VARCHAR PRIMARY KEY,
    latitudine Lat NOT NULL,
    longitudine Log NOT NULL
    -- v.incl (nome) occorre in Settore(falesia)
);


CREATE TABLE Settore (
    nome VARCHAR NOT NULL,
    esposizione coordinate NOT NULL,

    falesia VARCHAR NOT NULL,
    Foreign Key (falesia) 
        REFERENCES Falesia(nome),

    PRIMARY KEY (falesia, nome)
);


CREATE TABLE Grado (
    nome VARCHAR PRIMARY KEY,
    valore VARCHAR NOT NULL
);


CREATE TABLE Via (
    nome VARCHAR NOT NULL,
    lunghezza intgz NOT NULL,
    n_spit intgez NOT NULL,

    falesia VARCHAR NOT NULL,
    settore VARCHAR NOT NULL,
    Foreign Key (falesia, settore) 
        REFERENCES Settore(falesia, nome),

    grado VARCHAR NOT NULL,
    Foreign Key (grado) 
        REFERENCES Grado(nome),

    chiodatore VARCHAR NOT NULL,
    Foreign Key (chiodatore) 
        REFERENCES Chiodatore(persona),

    PRIMARY KEY (falesia, settore, nome)
);


CREATE TABLE Salita (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,

    arrampicatore VARCHAR NOT NULL,
    Foreign Key (arrampicatore) 
        REFERENCES Arrampicatore(persona),

    falesia VARCHAR NOT NULL,
    settore VARCHAR NOT NULL,
    via VARCHAR NOT NULL,
    Foreign Key (falesia, settore, via) 
        REFERENCES Via(falesia, settore, nome)
);


CREATE TABLE Flash (
    salita INTEGER NOT NULL,
    Foreign Key (salita) 
        REFERENCES Salita(id),

    PRIMARY KEY (salita)
);


CREATE TABLE AVista (
    salita INTEGER NOT NULL,
    Foreign Key (salita) 
        REFERENCES Salita(id),

    PRIMARY KEY (salita)
);


CREATE TABLE Ripetuta (
    salita INTEGER NOT NULL,
    Foreign Key (salita) 
        REFERENCES Salita(id),

    PRIMARY KEY (salita)
    -- v.incl (salita) occorre in Tentativo(ripetuta)
);


CREATE TABLE Tentativo (
    ripetuta INTEGER NOT NULL,
    Foreign Key (ripetuta) 
        REFERENCES Ripetuta(salita),

    PRIMARY KEY (ripetuta)
);