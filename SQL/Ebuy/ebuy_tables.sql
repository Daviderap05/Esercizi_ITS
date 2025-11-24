create table categoria (
	nome stringa primary key,
	super stringa
	    check (super <> nome)
);

alter table categoria add foreign key (super) references categoria(nome);

create table utente (
	username stringa primary key,
	registrazione timestamp not null
);

create table privato  (
	utente stringa primary key,
	foreign key (utente)
		references utente(username)
);

create table venditoreprof  (
	utente stringa primary key,
	vetrina url not null,
	unique(vetrina),
	foreign key (utente)
		references utente(username)
);

-- vincoli {disjoint, complete} su utente - Privato/VenditoreProf non ancora implementati

create table metododipagamento (
	nome stringa primary key
);

create table postoggetto (
	id serial primary key,
	pubblica stringa not null,
	unique(id, pubblica), -- chiave non-minimale, permette la foreign key da postoggettonuovo
	descrizione stringa not null,
	pubblicazione timestamp not null,
	ha_feedback boolean not null DEFAULT false,
	voto Voto,
	istante_feedback timestamp,
	commento stringa,
	categoria stringa not null,
	foreign key (categoria)
		references categoria(nome),
	foreign key (pubblica)
		references utente(username),

	check (
		(ha_feedback = true)
		=
		(voto is not null and istante_feedback is not null)
		),
	check (commento is null or ha_feedback = true),
	check (istante_feedback is null or istante_feedback > pubblicazione)

	-- v.incl. (id) occorre in met_post(postoggetto)
);

create table met_post(
	postoggetto integer not null,
	metodo stringa not null,
	primary key (postoggetto, metodo),
	foreign key (postoggetto)
		references postoggetto(id),
	foreign key (metodo)
		references metododipagamento(nome)
);

create table postoggettonuovo(
	postoggetto integer primary key,
	anni_garanzia intge2 not null,
	pubblica_nuovo stringa not null,

	foreign key (postoggetto, pubblica_nuovo)
		references postoggetto(id, pubblica), -- modella la IS-A tra associazioni

	foreign key (pubblica_nuovo)
		references venditoreprof(utente)
);

create table postoggettousato(
	postoggetto integer primary key,
	condizione condizione not null,
	anni_garanzia intgez not null,
	foreign key (postoggetto)
		references postoggetto(id)
);


create table postoggettoasta (
	postoggetto integer primary key,
	prezzo_base realgez not null,
	prezzo_bid realgz not null,
	scadenza timestamp not null,
	foreign key (postoggetto)
		references postoggetto(id)
);

create table postoggettocompralosubito (
	postoggetto integer primary key,
	prezzo realgz not null,
	foreign key (postoggetto)
		references postoggetto(id),
	acquirente stringa,
	istante_acquisto timestamp,
	foreign key (acquirente)
		references privato(utente),
	check (
		(acquirente is null) = (istante_acquisto is null)
	)
);

create table bid (
	codice serial primary key,
	istante timestamp not null,
	asta integer not null,
	unique(istante, asta),
	foreign key (asta)
		references postoggettoasta(postoggetto),
	privato stringa not null,
	foreign key (privato)
		references privato(utente)
);