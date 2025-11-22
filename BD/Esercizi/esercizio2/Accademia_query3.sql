-- Active: 1753297295466@@localhost@5432@accademia

-- QUERY 1 --
select posizione, count(*) 
from Persona 
GROUP BY posizione;


-- QUERY 2 --
select count(*) 
from persona 
where stipendio >= 40000;


-- QUERY 3 --
select count(*) 
from progetto 
where fine <= CURRENT_DATE 
    and budget > 50000;


-- QUERY 4 --
select avg(oreDurata), max(oreDurata), min(oreDurata) 
from AttivitaProgetto a, progetto p 
where p.id = a.progetto 
    and p.nome = 'Pegasus';


-- QUERY 5 --
select avg(oreDurata), max(oreDurata), min(oreDurata) 
from AttivitaProgetto a, progetto p 
where p.id = a.progetto 
    and p.nome = 'Pegasus';


-- QUERY 5 --
select per.id, per.nome, per.cognome, avg(oreDurata), max(oreDurata), min(oreDurata)
from persona per, AttivitaProgetto ap, progetto prg
where per.id = ap.persona 
    and prg.id = ap.progetto 
    and prg.nome = 'Pegasus'
GROUP BY (per.id)


-- QUERY 6 --
select per.id, per.nome, cognome, sum(oreDurata) as ore_didattica
from persona per, AttivitaNonProgettuale anp
where anp.persona = per.id
    and anp.tipo = 'Didattica'
GROUP BY(per.id)


-- QUERY 7 --
select avg(stipendio), max(stipendio), min(stipendio)
from persona
where posizione = 'Ricercatore'


-- QUERY 8 --
select posizione, avg(stipendio), max(stipendio), min(stipendio)
from persona p
where (p.posizione = 'Ricercatore'
    or p.posizione = 'Professore Associato'
    or p.posizione = 'Professore Ordinario')
GROUP BY(p.posizione)


-- QUERY 9 --
select pg.id, pg.nome, sum(oreDurata)
from persona p, AttivitaProgetto ap, progetto pg
where p.id = ap.persona
    and pg.id = ap.progetto
    and p.nome = 'Ginevra'
    and p.cognome = 'Riva'
GROUP BY (pg.id, pg.nome)


-- QUERY 10 --
SELECT pro.id, pro.nome as progetto
FROM Progetto pro, AttivitaProgetto ap  
WHERE pro.id = ap.progetto
GROUP BY(pro.nome, pro.id)
HAVING count(DISTINCT ap.persona) >= 2;


-- QUERY 11 --
SELECT p.id, p.nome, p.cognome
FROM persona p, attivitaprogetto ap
WHERE p.id = ap.persona
AND p.posizione = 'Professore Associato'
GROUP BY (p.id, p.nome, p.cognome)
HAVING count(DISTINCT ap.progetto) > 1;