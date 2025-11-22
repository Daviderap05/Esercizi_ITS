-- Active: 1753297295466@@localhost@5432@impiegati_studenti
create domain Stringa as varchar (200);

create domain CodiceFiscale as varchar(16);

create domain Data as date;

create domain IntGEZ as integer
        check (value >= 0);

create domain IntGZ as integer
        check (value > 0);

create domain RealGEZ as real
        check (value >= 0);

create type TipoProg as enum
        ('Progettista', 'Responsabile');