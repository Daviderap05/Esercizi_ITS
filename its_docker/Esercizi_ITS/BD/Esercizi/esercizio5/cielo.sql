-- Active: 1753341175299@@localhost@5432@cielo
create domain StringaM as varchar(100);

create domain PosInteger as integer check (value >= 0);

create domain codice_IATA as char(3);



create table Compagnia(

        nome StringaM primary key,
        annofondaz PosInteger
);


create table Aeroporto(

        codice codice_IATA primary key,
        nome StringaM not null
);


create table LuogoAeroporto(

        citta StringaM not null,
        nazione StringaM not null,

        aeroporto codice_IATA not null,
        foreign key (aeroporto)
                references Aeroporto(codice) deferrable,
        primary key (aeroporto)
);


alter table Aeroporto
        add foreign key (codice) references LuogoAeroporto(aeroporto) deferrable;


create table ArrPart(

        codice PosInteger not null, 
        comp StringaM not null,

        arrivo codice_IATA not null,
        partenza codice_IATA not null,
        
        foreign key (arrivo)
                references Aeroporto(codice),

        foreign key (partenza)
                references Aeroporto(codice),

        primary key (codice, comp)
);


create table Volo(

        codice PosInteger not null,
        durataMinuti PosInteger not null,
        
        -- accorpo compagnia
        comp StringaM not null,
        foreign key (comp)
                references Compagnia(nome),

        foreign key (codice, comp) 
                references ArrPart(codice, comp) deferrable,

        primary key (codice, comp)
);

alter table ArrPart
        add foreign key (codice, comp) references Volo(codice, comp) deferrable;