-- commento (per essere commento -- + spazio)
-- definizione delle tabelle

create table studente (
	matricola integer not null,
	nome varchar not null,
	primary key (matricola)
);


create table corso (
	nome varchar not null primary key,
	crediti integer not null
		check (crediti > 0)
);


create table esame (
	studente integer not null,
	corso varchar not null,
	data date not null,

	-- voto con vincolo di dominio
	voto integer not null
		check (voto >= 18 and voto <= 30),

	lode boolean not null,

	-- vincolo di ennupla
	-- if lode = true then voto = 30
	check (lode = false or voto = 30),
	
	foreign key (studente)
		references studente(matricola),
	foreign key (corso)
		references corso (nome),
	primary key (studente, corso)
);