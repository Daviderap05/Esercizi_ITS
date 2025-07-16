CREATE type Strutturato AS enum (	

	'Ricercatore', 
	'Professore Associato', 
	'Professore Ordinario'

);


CREATE type LavoroProgetto AS enum (	

	'Ricerca e Sviluppo', 
	'Dimostrazione', 
	'Management', 
	'Altro'

);


CREATE type LavoroNonProgettuale AS enum (	

	'Didattica', 
	'Ricerca', 
	'Missione', 
	'Incontro Dipartimentale', 
	'Incontro Accademico', 
	'Altro'

);


CREATE type CausaAssenza AS enum (	

	'Chiusura Universitaria', 
	'Maternita', 
	'Malattia'
);



CREATE DOMAIN PosInteger AS integer
	check (value is not null and value >= 0);


CREATE DOMAIN StringaM AS varchar (100)
	check (value is not null);


CREATE DOMAIN NumeroOre AS integer
	check (value is not null and value >= 0 and value <= 8);


CREATE DOMAIN Denaro AS real
	check (value is not null and value >= 0);


CREATE table Persona (

	id PosInteger not null,
	nome StringaM not null,
	cognome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null,

	primary key (id),

);


CREATE table Progetto (

	id PosInteger not null,
	nome StringaM not null unique,
	inizio date not null,
	fine date not null,
	budget Denaro not null,

	primary key (id),

	check (inizio < fine)

);


CREATE table WP (

	progetto PosInteger not null,
	id PosInteger not null,
	nome StringaM not null,
	inizio date not null,
	fine date not null,

	unique (progetto, nome),

	primary key (progetto, id),

	check (inizio < fine),

	foreign key (progetto)
		references Progetto(id)
);


CREATE table AttivitaProgetto (

	id PosInteger not null,
	persona PosInteger not null,
	progetto PosInteger not null,
	wp PosInteger not null,
	giorno date not null,
	tipo LavoroProgetto not null,
	oreDurata NumeroOre not null,

	primary key (id),

	foreign key (persona)
		references Persona(id),
	foreign key (progetto, wp)
		references 	WP(progetto, id)
);


CREATE table AttivitaNonProgettuale (

	id PosInteger not null,
	persona PosInteger not null,
	tipo LavoroNonProgettuale not null,
	giorno date not null,
	oreDurata NumeroOre not null,

	primary key (id),

	foreign key (persona)
		references Persona(id)

);


CREATE table Assenza (

	id PosInteger not null,
	persona PosInteger not null,
	tipo CausaAssenza not null,
	giorno date not null,

	unique (persona, giorno),

	primary key (id),

	foreign key (persona)
		references Persona(id)

);

-- (1, 'Davide', 'Raponi', 'Ricercatore', 1600)