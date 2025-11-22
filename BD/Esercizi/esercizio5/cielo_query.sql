-- ! QUERY 1 ! --

SELECT codice AS codice_volo, comp AS compagnia 
FROM Volo 
WHERE durataMinuti > 180;

-- ! QUERY 2 ! --

SELECT DISTINCT comp AS compagnia 
FROM Volo 
WHERE durataMinuti > 180;

-- ! QUERY 3 ! --

SELECT codice AS codice_volo, comp AS compagnia 
FROM arrpart 
WHERE partenza = 'CIA';

-- ! QUERY 4 ! --

SELECT DISTINCT comp AS compagnia 
FROM arrpart 
WHERE arrivo = 'FCO';

-- ! QUERY 5 ! --

SELECT DISTINCT codice AS codice_volo, comp AS compagnia 
FROM arrpart 
WHERE partenza = 'FCO' 
AND arrivo = 'JFK';

-- ! QUERY 6 ! --

SELECT DISTINCT comp AS compagnia 
FROM arrpart 
WHERE partenza = 'FCO' 
AND arrivo = 'JFK';

-- ! QUERY 7 ! --

SELECT DISTINCT comp AS compagnia 
FROM arrpart 
WHERE (partenza = 'FCO' OR partenza = 'CIA')
AND arrivo = 'JFK';

-- ! QUERY 8 ! --

SELECT DISTINCT luogoaeroporto.aeroporto AS codiceiata, aeroporto.nome, luogoaeroporto.citta, luogoaeroporto.nazione
FROM luogoaeroporto, aeroporto, arrpart
WHERE arrpart.comp = 'MagicFly'
AND arrpart.partenza = aeroporto.codice
AND aeroporto.codice = luogoaeroporto.aeroporto;

-- ! QUERY 9 ! --

SELECT codice, comp, partenza, arrivo 
FROM arrpart
WHERE (partenza = 'FCO' OR partenza = 'CIA')
AND arrivo = 'JFK';

-- ! QUERY 10 ! --

SELECT a.comp AS compagnia, a.codice AS codice_volo_1, a.partenza AS partenza, a.arrivo AS scalo, b.codice AS codice_volo_2, b.arrivo AS arrivo
FROM arrpart AS a, arrpart AS b
WHERE (a.partenza = 'FCO' or a.partenza = 'CIA')
AND a.arrivo = b.partenza
AND a.comp = b.comp 
AND b.arrivo = 'JFK';

-- ! QUERY 11 ! --

SELECT DISTINCT comp AS compagnia
FROM compagnia c, arrpart ap
WHERE c.nome = ap.comp
AND annofondaz IS NOT NULL;

-- QUERY EXTRA --

select count(*) from luogoaeroporto, volo, arrpart
where luogoaeroporto.citta = 'Roma'
and volo.durataminuti >= 180
AND luogoaeroporto.aeroporto = arrpart.partenza
AND arrpart.codice = volo.codice 
and arrpart.comp = volo.comp;