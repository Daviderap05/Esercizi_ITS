create table Posizione_Militare(

    nome Stringa PRIMARY KEY
);

create table Persona (

    cf CodiceFiscale PRIMARY KEY,
    nome Stringa not null,
    cognome Stringa not null,
    nascita Data not null
);

create table Uomo(

    uomo CodiceFiscale PRIMARY KEY,
    pos_militare Stringa not null,

    Foreign Key (uomo) 
        REFERENCES Persona(cf),
    Foreign Key (pos_militare) 
        REFERENCES Posizione_Militare(nome)
);

create table Donna(

    donna CodiceFiscale PRIMARY KEY,
    maternita IntGEZ not null,

    Foreign Key (donna) 
        REFERENCES Persona(cf)
);

create table Studente(

    matricola IntGEZ not null,

    studente CodiceFiscale not null,
    Foreign Key (studente) 
        REFERENCES Persona(cf),

    PRIMARY KEY (studente, matricola)
);

create table Impiegato(

    impiegato CodiceFiscale PRIMARY KEY,
    stipendio RealGEZ not null,
    
    Foreign Key (impiegato) 
        REFERENCES Persona(cf)  
);

create table Segretario(

    segretario CodiceFiscale PRIMARY KEY,
    
    Foreign Key (segretario) 
        REFERENCES Impiegato(impiegato)  
);

create table Direttore(

    direttore CodiceFiscale PRIMARY KEY,
    
    Foreign Key (direttore) 
        REFERENCES Impiegato(impiegato)  
);

create table Progettista(

    progettista CodiceFiscale PRIMARY KEY,
    tipo TipoProg not null,

    Foreign Key (progettista) 
        REFERENCES Impiegato(impiegato)  
);

-- create table Responsabile(

--     responsabile CodiceFiscale PRIMARY KEY,
    
--     Foreign Key (responsabile) 
--         REFERENCES Progettista(progettista)  
-- );

create table Progetto(

    id serial PRIMARY KEY,
    nome Stringa not null
);

create table resp_prog(

    progettista CodiceFiscale not null,
    progetto integer not null,

    Foreign Key (progettista) 
        REFERENCES Progettista(progettista),
    Foreign Key (progetto) 
        REFERENCES Progetto(id),

    PRIMARY KEY (progettista)
);