-- Active: 1753297295466@@localhost@5432@impiegati_studenti2@public
-- query 1
select p.nome from impiegato i, persona p where i.persona = p.cf and p.nascita >= '1965-01-01';


-- query 2
select nome from progetto;


-- query 3
select stipendio from impiegato i where i.ruolo = 'Direttore';


-- query 4
select count(impiegato) from impiegato where ruolo = 'Progettista';


-- query 5
select count(impiegato) from responsabile;


-- query 6
select count(i) from impiegato i where i.ruolo = 'Progettista' and i.persona not in (select impiegato from responsabile);


--query 7
select avg(stipendio) from impiegato where ruolo = 'Segretario';


-- query 8
select max(date_part('year', age(current_date, nascita))) as eta from persona p, studente s where s.persona = p.cf;


-- query 9
select count(i) from impiegato i, persona p where i.persona = p.cf and p.pos_mil = 'Assolto' and i.ruolo = 'Direttore';


-- query 10
select count(distinct progetto) from resp_prog rp, persona p where p.cf = rp.responsabile and p.maternita >= 2