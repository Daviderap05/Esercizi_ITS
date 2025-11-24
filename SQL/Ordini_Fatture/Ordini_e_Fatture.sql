-- Active: 1753341175299@@localhost@5432@ordinifatture
create domain Stringa as varchar(200);

create domain IntGEZ as integer
        check (value >= 0);

create domain RealGEZ as real
        check (value >= 0);

create domain CAP as char(5)
        check (value ~ '[0-9]{5}');

create type Indirizzo as (
        via Stringa,
        cap CAP,
        civico Stringa
);

create domain CodiceFiscale as varchar(16);

create domain PartitaIVA as varchar(11);

create domain real_In_0_1 as real
        check(value >= 0 and value <= 1);

create type StatoOrdine as enum (

        'In preparazione',
        'Inviato',
        'Da saldare',
        'Saldato'
);

create domain Telefono as varchar (15);

create domain Email as varchar(100)
        check (value ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}$');


create table nazione(

        nome_nazione Stringa primary key
);


create table regione(

        nome_nazione Stringa not null,
        nome_regione Stringa not null,

        foreign key (nome_nazione)
                references nazione(nome_nazione),

        primary key(nome_nazione, nome_regione)
);


create table citta(

        id_citta serial primary key,
        nome_citta Stringa not null,

        nome_nazione Stringa not null,
        nome_regione Stringa not null,

        foreign key (nome_nazione, nome_regione)
                references regione(nome_nazione, nome_regione),

        unique (nome_nazione, nome_regione, nome_citta)
);


create table direttore(

        cf_direttore CodiceFiscale primary key,
        nome Stringa not null,
        cognome Stringa not null,
        data_nascita date not null,
        anni_servizio IntGEZ not null,

        citta integer not null,
        foreign key (citta)
                references citta(id_citta)
);


create table fornitore (

        id_fornitore serial primary key,
        ragione_sociale Stringa not null,
        PartitaIVA PartitaIVA not null,
        Indirizzo Indirizzo not null,
        Telefono Telefono not null,
        Email email not null,

        citta integer not null,
        foreign key (citta)
                references citta(id_citta)
);


create table dipartimento(

        nome_dipartimento Stringa primary key,
        Indirizzo Indirizzo not null,

        cf_direttore CodiceFiscale not null,
        foreign key (cf_direttore)
                references direttore(cf_direttore),

        citta integer not null,
        foreign key (citta)
                references citta(id_citta)
);


create table ordine(

        id_ordine serial primary key,
        data_stipula date not null,
        imponibile RealGEZ not null,
        aliquota_iva real_In_0_1 not null,
        stato StatoOrdine not null,

        nome_dipartimento Stringa not null,
        foreign key (nome_dipartimento)
                references dipartimento(nome_dipartimento),

        id_fornitore integer not null,
        foreign key (id_fornitore)
                references fornitore(id_fornitore)
);