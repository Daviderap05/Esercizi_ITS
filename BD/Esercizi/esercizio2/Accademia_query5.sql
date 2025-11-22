-- QUERY 1 --
SELECT *
FROM Persona
WHERE stipendio <= 40000


-- QUERY 2 --
SELECT *
FROM Persona p, AttivitaProgetto a
WHERE p.id = a.persona
AND posizione = 'Ricercatore'
AND stipendio <= 45000


-- QUERY 3 --
select sum(budget)
from Progetto


-- QUERY 4 --
SELECT p.nome, p.cognome, sum(budget)
FROM Persona p, AttivitaProgetto a, Progetto pr
WHERE p.id = a.persona
AND a.progetto = pr.id
GROUP BY p.id, p.nome, p.cognome


-- QUERY 5 --
SELECT p.nome, p.cognome, count(*)
FROM Persona p, AttivitaProgetto a
WHERE p.id = a.persona
AND p.posizione = 'Professore Ordinario'
GROUP BY p.id, p.nome, p.cognome


-- QUERY 6 --
SELECT p.nome, p.cognome, count(*)
FROM Persona p, Assenza a
WHERE p.id = a.persona
AND p.posizione = 'Professore Associato'
GROUP BY p.id


-- QUERY 7 --
SELECT p.nome, p.cognome, sum(oreDurata)
FROM Persona p, AttivitaProgetto a
WHERE p.id = a.persona
AND a.progetto = '1'
GROUP BY p.id


-- QUERY 8 --
SELECT p.nome, p.cognome, avg(oreDurata)
FROM Persona p, AttivitaProgetto a
WHERE p.id = a.persona
GROUP BY p.id   


-- QUERY 9 --
SELECT p.nome, p.cognome, sum(oreDurata) 
FROM Persona p, AttivitaNonProgettuale a
WHERE p.id = a.persona
AND a.tipo = 'Didattica'
GROUP BY p.id


-- QUERY 10 --
SELECT p.nome, p.cognome, sum(oreDurata) 
FROM Persona p, AttivitaProgetto a
WHERE p.id = a.persona
AND a.wp = '0'
AND a.progetto = '1'
GROUP BY p.id