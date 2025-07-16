CREATE DOMAIN stringa AS varchar(200)
	check(value is not null);


CREATE DOMAIN realGEZ AS real
	check (value is not null and value >= 0);


CREATE TYPE indirizzo AS(

	via stringa,
	civico stringa

);



CREATE TABLE impiegato(

	id integer primary key,

	nome stringa not null,
	cognome stringa not null,
	nascita date not null,
	stipendio realGEZ not null

);


CREATE TABLE dipartimento(

	id integer primary key,

	nome stringa not null,
	indirizzo indirizzo,

	impiegato integer not null,

	foreign key (impiegato)
		references impiegato(id)

	-- v.incl id occorre almeno una volta in dip_tel(id_dipartimento)

);


CREATE TABLE telefono(

	telefono varchar(15) primary key
	-- v.incl telefono occorre almeno una volta in dip_tel(id_telefono)
	
);


CREATE TABLE dip_tel(

	id_telefono varchar(15) not null,
	id_dipartimento integer not null,

	foreign key (id_telefono)
		references telefono(telefono),

	foreign key (id_dipartimento)
		references dipartimento(id),

	primary key (id_dipartimento, id_telefono)

);


CREATE TABLE progetto(

	id integer primary key,

	nome stringa not null,
	budget realGEZ not null

);


CREATE TABLE coinvolto(

	impiegato integer not null,
	progetto integer not null,


	foreign key (impiegato)
		references impiegato(id),

	foreign key (progetto)
		references progetto(id),

	primary key(impiegato, progetto)

);


CREATE TABLE afferenza(

	impiegato integer not null,
	dipartimento integer not null,
	data_afferenza date not null,

	foreign key (impiegato)
		references impiegato(id),

	foreign key (dipartimento)
		references dipartimento(id),

	unique (dipartimento),
	primary key(impiegato)

);