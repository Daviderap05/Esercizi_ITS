-- QUERY 1 --
select distinct cognome 
from persona;


-- QUERY 2 --
select nome, cognome 
from persona
where posizione = 'Ricercatore';


-- QUERY 3 --
select cognome 
from persona 
where posizione = 'Professore Associato' 
and cognome like 'V%';


-- QUERY 4 --
select cognome 
from persona 
where (posizione = 'Professore Associato' 
    or posizione = 'Professore Ordinario') 
    and cognome like 'V%';


-- QUERY 5 --
select nome 
from progetto
where fine < current_date;


-- QUERY 6 --
select nome
from progetto 
order by inizio;


-- QUERY 7 --
select nome 
from wp 
order by nome asc;


-- QUERY 8 --
select distinct tipo 
from assenza;


-- QUERY 9 --
select distinct tipo 
from attivitaprogetto;


-- QUERY 10 --
select distinct giorno
from attivitanonprogettuale
where tipo = 'Didattica' 
order by giorno asc;