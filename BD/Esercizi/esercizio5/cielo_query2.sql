-- Active: 1753297295466@@localhost@5432@cielo
-- Query 1 --
select a.codice, a.nome, count(distinct ap.comp)
from Aeroporto a, ArrPart ap
where a.codice = ap.partenza
    or a.codice = ap.arrivo
GROUP BY (a.codice, a.nome)


-- Query 2 --
select count(v.codice)
from volo v, ArrPart ap
where v.codice = ap.codice
    and v.comp = ap.comp
    and ap.partenza = 'HTR'
    and v.durataMinuti >= '100'


-- Query 3 --
select la.nazione, count(distinct la.aeroporto)
from LuogoAeroporto la, ArrPart ap
where (la.aeroporto = ap.partenza
    or la.aeroporto = ap.arrivo)
    and ap.comp = 'Apitalia'
GROUP BY(la.nazione)


-- Query 4 --
select round(avg(durataMinuti)::numeric, 1), max(durataMinuti), min(durataMinuti)
from volo
where volo.comp = 'MagicFly'


-- Query 5 --
select a.codice, a.nome, min(c.annofondaz)
from Compagnia c, ArrPart ap, Aeroporto a
where c.nome = ap.comp
    and (a.codice = ap.partenza
    or a.codice = ap.arrivo)
GROUP BY (a.codice, a.nome)


-- Query 6 --
SELECT la1.nazione AS nazione, COUNT(DISTINCT la2.nazione) AS raggiungibili
FROM ArrPart ap, LuogoAeroporto la1, LuogoAeroporto la2
WHERE ap.partenza = la1.aeroporto
  AND ap.arrivo   = la2.aeroporto
  AND la1.nazione <> la2.nazione
GROUP BY la1.nazione;


-- Query 7 --
select a.codice, a.nome, avg(v.durataMinuti)
from Aeroporto a, Volo v, ArrPart ap
where a.codice = ap.partenza
    and v.codice = ap.codice
group by a.codice, a.nome


-- Query 8 --
select v.comp, sum(durataMinuti) as durata_tot
from Volo v, Compagnia c
where c.nome = v.comp
    and c.annofondaz >= '1950'
group by v.comp


-- Query 9 --
select a.codice, a.nome
from Aeroporto a, ArrPart ap
where (a.codice = ap.partenza
    or a.codice = ap.arrivo)
GROUP BY (a.codice, a.nome)
HAVING count(distinct ap.comp) = 2


-- Query 10 --
select la.citta
from LuogoAeroporto la
GROUP BY citta
HAVING count(aeroporto) >= 2


-- Query 11 --
select comp as compagnia
from volo
GROUP BY comp
HAVING avg(volo.durataMinuti) > 360


-- Query 12 --
select comp as compagnia
from volo
GROUP BY comp
HAVING min(volo.durataMinuti) > 100