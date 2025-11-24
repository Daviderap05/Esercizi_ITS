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


-- ============= PERSONE (UOMINI) =============
insert into persona (cf, nome, cognome, nascita, genere, pos_mil)
values
('BRNSLV82C12H501A', 'Silvano', 'Bruni', '1982-03-12', 'Uomo', 'Assolto'),
('CNTLRA95D05H501B', 'Lorenzo', 'Conti', '1995-04-05', 'Uomo', 'Non assolto'),
('FRRCLD79H22H501C', 'Claudio', 'Ferrari', '1979-06-22', 'Uomo', 'Obiettore di coscienza'),
('GLLMRC90A10H501D', 'Marco', 'Galli', '1990-01-10', 'Uomo', 'Assolto'),
('RCCGNN84B28H501E', 'Gennaro', 'Ricci', '1984-02-28', 'Uomo', 'Non tenuto'),
('MRTFDE88L03H501F', 'Fedele', 'Martini', '1988-07-03', 'Uomo', 'Assolto'),
('RSSLNZ93E14H501G', 'Lorenzo', 'Rossi', '1993-05-14', 'Uomo', 'Non tenuto'),
('BTTFNC76M09H501H', 'Fabrizio', 'Batti', '1976-08-09', 'Uomo', 'Assolto'),
('NSTCRL99T30H501I', 'Carlo', 'Neri', '1999-09-30', 'Uomo', 'Non assolto');

-- ============= PERSONE (DONNE) =============
insert into persona (cf, nome, cognome, nascita, genere, maternita)
values
('VRDLRA85R15H501J', 'Lara', 'Verdi', '1985-10-15', 'Donna', 2),
('FRNSRA92C01H501K', 'Sara', 'Ferri', '1992-03-01', 'Donna', 1),
('BNCGNS81S21H501L', 'Ginevra', 'Bianchi', '1981-11-21', 'Donna', 3),
('MRTLRA00E02H501M', 'Laura', 'Martel', '2000-05-02', 'Donna', 0),
('RSSLIA97M18H501N', 'Lia', 'Rossi', '1997-08-18', 'Donna', 0),
('CNTFRN03L07H501O', 'Francesca', 'Contini', '2003-07-07', 'Donna', 0),
('GLLSLL89H12H501P', 'Stella', 'Gallo', '1989-06-12', 'Donna', 1),
('NSTRBH94A25H501Q', 'Rebecca', 'Nastro', '1994-01-25', 'Donna', 2),
('LMBMNL86D04H501R', 'Manuela', 'Lombardi', '1986-04-04', 'Donna', 1);

-- ============= STUDENTI =============
insert into studente (persona, matricola)
values
('MRTLRA00E02H501M', 3),
('CNTFRN03L07H501O', 4),
('NSTRBH94A25H501Q', 5),
('RSSLIA97M18H501N', 6),
('GLLSLL89H12H501P', 7),
('FRNSRA92C01H501K', 8);

-- ============= IMPIEGATI =============
insert into impiegato (persona, stipendio, ruolo)
values
('BRNSLV82C12H501A', 38000, 'Segretario'),
('CNTLRA95D05H501B', 29000, 'Progettista'),
('FRRCLD79H22H501C', 52000, 'Direttore'),
('GLLMRC90A10H501D', 41000, 'Progettista'),
('RCCGNN84B28H501E', 36000, 'Segretario'),
('MRTFDE88L03H501F', 47000, 'Progettista'),
('RSSLNZ93E14H501G', 32000, 'Progettista'),
('BTTFNC76M09H501H', 60000, 'Direttore'),
('NSTCRL99T30H501I', 30000, 'Segretario'),
('VRDLRA85R15H501J', 35000, 'Progettista'),
('BNCGNS81S21H501L', 34000, 'Segretario'),
('LMBMNL86D04H501R', 39000, 'Progettista');

-- ============= RESPONSABILI =============
insert into responsabile (impiegato)
values
('CNTLRA95D05H501B'),
('GLLMRC90A10H501D'),
('MRTFDE88L03H501F'),
('RSSLNZ93E14H501G'),
('VRDLRA85R15H501J'),
('LMBMNL86D04H501R');

-- ============= ASSEGNAZIONE RESPONSABILI → PROGETTI =============
insert into resp_prog (responsabile, progetto)
values
('CNTLRA95D05H501B', 1),
('CNTLRA95D05H501B', 2),
('GLLMRC90A10H501D', 2),
('MRTFDE88L03H501F', 3),
('RSSLNZ93E14H501G', 4),
('VRDLRA85R15H501J', 5),
('LMBMNL86D04H501R', 1),
('LMBMNL86D04H501R', 4);

-- Nuovi Progettisti NON responsabili
insert into persona (cf, nome, cognome, nascita, genere, pos_mil)
values
('CSTFNC85A01H501S', 'Franco', 'Costa', '1985-01-01', 'Uomo', 'Non assolto');

insert into persona (cf, nome, cognome, nascita, genere, maternita)
values
('BLLLRA91B15H501T', 'Laura', 'Belli', '1991-02-15', 'Donna', 1);

insert into impiegato (persona, stipendio, ruolo)
values
('CSTFNC85A01H501S', 31000, 'Progettista'),
('BLLLRA91B15H501T', 29500, 'Progettista');