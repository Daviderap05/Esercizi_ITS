-- Active: 1753297295466@@localhost@5432@accademia

-- QUERY 1 --
SELECT * 
FROM Progetto
WHERE fine > '2003-12-31';


-- QUERY 2 --
SELECT count(*), posizione
FROM Persona
GROUP BY posizione;


-- QUERY 3 --
SELECT DISTINCT p.id, p.nome
FROM Persona p, Assenza a
WHERE p.id = a.persona
AND a.tipo = 'Malattia';


-- QUERY 4 --
SELECT count(*), a.tipo
FROM Persona p, Assenza a
WHERE p.id = a.persona
GROUP BY a.tipo


-- QUERY 5 --
select max(stipendio)
FROM Persona
WHERE posizione = 'Professore Ordinario';


-- QUERY 6 --
select id, tipo, oredurata
FROM AttivitaProgetto
WHERE persona = '10'
AND progetto = '1'
ORDER BY oredurata DESC;


-- QUERY 7 --
select DISTINCT p.id, p.nome, p.cognome, a.tipo, count(*)
FROM Persona p, Assenza a
WHERE p.id = a.persona
GROUP BY p.id, p.nome, p.cognome, a.tipo


-- QUERY 8 --
SELECT id, nome, cognome
FROM Persona
WHERE posizione = 'Professore Ordinario'
AND stipendio = (SELECT max(stipendio)
                    FROM Persona
                    WHERE posizione = 'Professore Ordinario');



-- QUERY 9 --
SELECT sum(oreDurata)
FROM AttivitaProgetto
WHERE persona = '0'
AND oreDurata < 10
GROUP BY persona;


-- QUERY 10 --
select *
FROM Persona p
WHERE p.id NOT IN (
    SELECT a.persona
    FROM assenza a
    WHERE a.tipo = 'Chiusura Universitaria'
)