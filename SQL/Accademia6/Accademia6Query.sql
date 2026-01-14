-- Active: 1764194045216@@localhost@5432@rocklog
-- QUERY 1 --
SELECT posizione, count(*)
FROM Persona
GROUP BY posizione


-- QUERY 2 --
SELECT count(*)
FROM Persona
WHERE stipendio >= 40000


-- QUERY 3 --
SELECT count(*)
FROM Progetto
WHERE fine IS NOT NULL
    AND budget > 50000


-- QUERY 4 --
SELECT round(avg(oreDurata), 2) as media, max(oreDurata), min(oreDurata)
FROM AttivitaProgetto ap, Progetto p
WHERE ap.progetto = p.id 
    AND p.nome = 'Pegasus'


-- QUERY 5 --
SELECT round(avg(oreDurata), 2) as media, max(oreDurata), min(oreDurata)
FROM AttivitaProgetto ap, Progetto p
WHERE ap.progetto = p.id 
    AND p.nome = 'Pegasus'
GROUP BY ap.persona


-- QUERY 6 --
SELECT nome, cognome, sum(oreDurata)
FROM Persona p, AttivitaNonProgettuale ap
WHERE p.id = ap.persona
    AND ap.tipo = 'Didattica'
GROUP BY p.nome, p.cognome, ap.persona


-- QUERY 7 --
SELECT avg(stipendio) as media, max(stipendio), min(stipendio)
FROM Persona
WHERE posizione = 'Ricercatore'


-- QUERY 8 --
SELECT posizione, avg(stipendio) as media, max(stipendio), min(stipendio)
FROM Persona
GROUP BY posizione


-- QUERY 9 --
SELECT pg.nome, sum(ap.oreDurata)
FROM Persona p, AttivitaProgetto ap, progetto pg
WHERE p.nome = 'Ginevra'
    AND p.cognome = 'Riva'
    AND p.id = ap.persona
    AND pg.id = ap.progetto
GROUP BY ap.progetto, pg.nome


-- QUERY 10 --
SELECT p.nome
FROM AttivitaProgetto ap, progetto p
WHERE ap.progetto = p.id
GROUP BY p.id, p.nome
HAVING count(ap.persona) > 2


-- QUERY 11 --
SELECT p.nome, p.cognome, count(*)
FROM persona p, AttivitaProgetto ap
WHERE p.id = ap.persona
    AND p.posizione = 'Professore Ordinario'
GROUP BY p.id
HAVING count(*) > 1