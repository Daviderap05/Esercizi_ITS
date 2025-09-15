-- Active: 1753297295466@@localhost@5432@impiegati_studenti2

insert into posizionemilitare(nome)
values
('Obiettore di coscienza'),
('Non assolto'),
('Assolto'),
('Non tenuto');


insert into persona(cf, nome, cognome, nascita, genere, pos_mil)
values
('RSSMRA77F10H501L', 'Mario', 'Rossi', '1977-06-10', 'Uomo', 'Assolto'),
('VRDGPP89A31H501X', 'Giuseppe', 'Verdi', '1989-01-31', 'Uomo', 'Non tenuto');


insert into persona(cf, nome, cognome, nascita, genere, maternita)
values
('BNCMRA62R58F839Y', 'Maria', 'Bianchi', '1962-07-28', 'Donna', 4),
('DRCGNN01T48C678K', 'Giovanna', 'D''Arco', '2001-09-16', 'Donna', 0);


insert into studente(persona, matricola)
values
('VRDGPP89A31H501X', '1'),
('DRCGNN01T48C678K', '2');


insert into impiegato(persona, stipendio, ruolo)
values
('RSSMRA77F10H501L', 45000, 'Direttore'),
('BNCMRA62R58F839Y', 33000, 'Progettista');


insert into responsabile(impiegato)
values
('BNCMRA62R58F839Y');


insert into progetto(nome)
values
('Phoenix'),
('Pegaso'),
('Manhattan'),
('ITiEsse'),
('Gladio') 
returning id;

insert into resp_prog(responsabile, progetto)
values
('BNCMRA62R58F839Y', 3),
('BNCMRA62R58F839Y', 5);