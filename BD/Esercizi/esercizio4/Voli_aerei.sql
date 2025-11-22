create domain str as varchar(200);

create domain IntGEZ as integer
        check (value >= 0);
        
create domain IntGZ as integer
        check (value > 0);

create domain IntGE1900 as integer
        check (value >= 1900);

create domain codice_volo as varchar(6);

create domain codice_IATA as varchar(3);



create table nazione(

	nome str primary key
);


create table città(

	nome_città str not null,
	n_abitanti IntGEZ not null,

	-- accorpo  nazione 
	nome_nazione str not null,
	foreign key (nome_nazione)
		references nazione(nome),

	primary key(nome_nazione, nome_città)
);


create table aereoporto(

	id serial primary key,
	codice_IATA codice_IATA not null,
	nome str not null,

	-- accorop aer_città
	nome_città str not null,
	nome_nazione str not null,
	foreign key (nome_nazione, nome_città)
		references città(nome_nazione, nome_città)
);


create table compagnia(

	id serial primary key,
	nome str not null,
	fondazione IntGE1900 not null,

	-- accorop comp_cit
	nome_città str not null,
	nome_nazione str not null,
	foreign key (nome_nazione, nome_città)
		references città(nome_nazione, nome_città)
);


create table volo(

	id serial primary key,
	id_volo	 codice_volo not null,
	durata_minuti IntGZ,

	-- accorpo arrivo
	arrivo integer not null,
	foreign key (arrivo)
		references aereoporto(id),

	-- accorpo partenza
	partenza integer not null,
	foreign key (partenza)
		references aereoporto(id),

	-- accorpo volo_comp
	codice_compagnia integer,
	foreign key (codice_compagnia)
		references compagnia(id)
);