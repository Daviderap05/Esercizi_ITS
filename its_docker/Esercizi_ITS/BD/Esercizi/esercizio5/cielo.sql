create domain StringaM as varchar(100);

create domain PosInteger as integer check (value >= 0);

create domain codice_IATA as char(3);



create table Compagnia(

        nome StringaM primary key,
        anno_fondazione PosInteger
);


create table Aereoporto(

        codiceIATA codice_IATA primary key,
        nome StringaM not null
);


create table LuogoAeroporto(

        città StringaM not null,
        nazione StringaM not null,

        codiceIATA codice_IATA not null,
        foreign key (codiceIATA)
                references Aereoporto(codiceIATA),

        primary key (codiceIATA)
);


-- alter table Aeroporto
-- add foreign key (codice) references LuogoAeroporto(aeroporto);


create table ArrPart(

        codice PosInteger not null, 
        comp StringaM not null,

        arrivo codice_IATA not null,
        foreign key (arrivo)
                references Aereoporto(codiceIATA),

        partenza codice_IATA not null,
        foreign key (partenza)
                references Aereoporto(codiceIATA),

        primary key (codice, comp)
);


create table Volo(

        codice PosInteger not null,
        durata_minuti PosInteger not null,
        
        -- accorpo compagnia
        comp StringaM not null,
        foreign key (comp)
                references Compagnia(nome),

        foreign key (codice, comp) 
                references ArrPart(codice, comp),

        primary key (codice, comp)
);

-- alter table ArrPart
-- add foreign key (codice, comp) references Volo(codice, comp);