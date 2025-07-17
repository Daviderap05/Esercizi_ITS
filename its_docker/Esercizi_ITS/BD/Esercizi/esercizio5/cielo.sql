create domain StringaM as varchar(100);

create domain PosInteger as integer
        check (value >= 0);

create domain codice_IATA as char(3);



create table Compagnia(

        nome StringaM primary key,
        anno_fondazione PosInteger
);


create table Volo(

        codice PosInteger not null,
        durata_minuti PosInteger not null,
        
        -- accorpo compagnia
        comp StringaM not null,
        foreign key (comp)
                references Compagnia(nome),

        primary key (codice, comp)
);


create table Aereoporto(

        codice codice_IATA primary key,
        nome StringaM not null,
);


create table LuogoAeroporto(

        città StringaM not null,
        nazione StringaM not null,

        codice codice_IATA not null,
        foreign key (codice)
                references Aereoporto(codice),

        primary key (codice, città)
);


create table ArrPart(

        codice PosInteger primary key, 
        comp StringaM not null,

        arrivo CodIATA not null,
        foreign key (arrivo)
                references Aereoporto(arrivo),

        partenza CodIATA not null,
        foreign key (partenza)
                references Aereoporto(partenza)
);