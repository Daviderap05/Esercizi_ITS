-- QUERY 1 --
SELECT *
FROM areaverde a, soggettoverde s
WHERE a.id = s.id
    AND s.specie = 'Pinus pinea'
    AND s.data < CURRENT_DATE - INTERVAL '5 year'


-- QUERY 2 --
SELECT *
FROM areaverde a
WHERE a.is_sensibile = TRUE
  AND a.id NOT IN (
    SELECT i.id
    FROM intervento i, interventoassegnato ia
    WHERE ia.intervento = i.id
        AND (i.inizio, ia.fine) OVERLAPS ('2023-10-09', '2023-10-13')
  );


-- QUERY 3 --
WITH conteggi AS (
  SELECT
      o.cf,
      COUNT(DISTINCT a.interventoassegnato) AS n_interventi
  FROM operatore o, assegna a, interventoassegnato ia, intervento i
  WHERE a.operatore = o.cf
    AND ia.intervento = a.interventoassegnato
    AND i.id = ia.intervento
    AND i.priorità >= 5
    AND i.inizio >= DATE '2023-01-01'
    AND i.inizio <  DATE '2024-01-01'
  GROUP BY o.cf
)
SELECT o.*
FROM operatore o, conteggi c
WHERE c.cf = o.cf
  AND c.n_interventi = (SELECT MIN(n_interventi) FROM conteggi);


-- QUERY 4 --
SELECT *
FROM areaverde a, soggettoverde s
WHERE a.id = s.id
GROUP BY a.id, s.id
HAVING count(s.id) >= 10

-- QUERY 5 --
SELECT DISTINCT count(a.operatore) as conteggio
FROM intervento i, assegna a
WHERE a.interventoAssegnato = i.id
  and i.priorità < 4
  GROUP BY i.id, a.operatore, a.interventoAssegnato

-- QUERY 6 --
SELECT i.id, avg(i.durata), avg(ia.fine - i.inizio)
FROM intervento i, interventoassegnato ia
where i.id = ia.intervento
  and ia.fine IS NOT NULL
GROUP BY i.id

-- QUERY 7 --
WITH tab AS (
  SELECT *, (ia.fine - a.istante) AS massimo
  FROM assegna a, interventoassegnato ia
  WHERE a.interventoassegnato = ia.intervento
    AND ia.fine IS NOT NULL
)
SELECT *
FROM tab
WHERE massimo = (SELECT max(massimo) FROM tab);
