-- Active: 1753341175299@@localhost@5432@accademia@public
-- QUERY 1 --

select wp.id, wp.nome, wp.inizio, wp.fine 
from wp, progetto p 
where p.nome = 'Pegasus' 
    and wp.progetto = p.id;

-- QUERY 2 --

select distinct p.id, p.nome, p.cognome, p.posizione 
from persona p, progetto pr, attivitaprogetto ap
where pr.id = ap.progetto 
    and ap.persona = p.id
    and pr.nome = 'Pegasus'
order by cognome desc;

-- QUERY 3 --

select distinct p.id, p.nome, p.cognome, p.posizione 
from persona p, progetto pr, attivitaprogetto ap
where pr.id = ap.progetto 
    and ap.persona = p.id
    and pr.nome = 'Pegasus'
group by p.id, p.nome, p.cognome, p.posizione
    having(count(ap.persona) > 1);

-- QUERY 4 --

select distinct p.id, p.nome, p.cognome 
from assenza a, persona p 
where p.id = a.persona 
    and p.posizione = 'Professore Ordinario' 
    and a.tipo = 'Malattia';

-- QUERY 5 --

select p.id, p.nome, p.cognome 
from assenza a, persona p 
where p.id = a.persona 
    and p.posizione = 'Professore Ordinario' 
    and a.tipo = 'Malattia' 
group by (p.id, p.nome, p.cognome) 
    having count(a.persona) > 1;

-- QUERY 6 --

select distinct p.id, p.nome, p.cognome 
from persona p, attivitanonprogettuale anp 
where anp.persona = p.id 
    and anp.tipo = 'Didattica' 
    and p.posizione = 'Ricercatore' 
order by p.id desc;

-- QUERY 7 --

select p.id, p.nome, p.cognome 
from persona p, attivitanonprogettuale anp 
where anp.persona = p.id 
    and anp.tipo = 'Didattica' 
    and p.posizione = 'Ricercatore' 
group by(p.id, p.nome, p.cognome) 
    having count(anp.persona) > 1;

-- QUERY 8 --

select distinct p.id, p.nome, p.cognome 
from persona p, attivitaprogetto ap, attivitanonprogettuale anp 
where ap.persona = p.id 
    and anp.persona = p.id 
    and ap.giorno = anp.giorno;

-- QUERY 9 --

select p.id, p.nome, p.cognome, ap.giorno, pr.nome as prj, ap.oredurata as h_prj, anp.tipo as att_noprj, anp.oredurata as h_noprj 
from persona p, attivitaprogetto ap, attivitanonprogettuale anp, progetto pr
where ap.persona = p.id 
    and anp.persona = p.id 
    and ap.giorno = anp.giorno
    and pr.id = ap.progetto;

-- QUERY 10 --

select distinct p.id, p.nome, p.cognome 
from persona p, assenza a, attivitaprogetto ap
where p.id = a.persona
and a.giorno = ap.giorno
and p.id = ap.persona;

-- QUERY 11 --

select distinct p.id, p.nome, p.cognome, ap.giorno, a.tipo as causa_ass, pr.nome as progetto, ap.oreDurata as ore_att_prj
from persona p, assenza a, attivitaprogetto ap, progetto pr
where p.id = a.persona
and a.giorno = ap.giorno
and p.id = ap.persona
and pr.id = ap.progetto;

-- QUERY 12 --

select wp.nome 
from wp, progetto p
where p.id = wp.progetto
group by (wp.nome) 
    having count(distinct wp.progetto) > 1;