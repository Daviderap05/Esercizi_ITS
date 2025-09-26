-- Estensioni utili (facoltative)
create extension if not exists pgcrypto; -- per UUID in futuro

-- =========================
-- TABELLA: Sessione
-- =========================

create table sessione (
  id          serial primary key,
  nome        text        not null,
  data        date        not null,
  is_active   boolean     not null default true,
  create_at   timestamptz not null default now()
);

-- =========================
-- TABELLA: Cantante
-- =========================

create table cantante (
  id           serial primary key,
  nome         text    not null,
  ha_usb       boolean not null default false,
  sessione_id  int     not null references sessione(id) on delete cascade,
  create_at    timestamptz not null default now()
);

-- =========================
-- TABELLA: Canzone
-- =========================

create table canzone (
  id_canzone serial primary key,
  titolo     text not null,
  artista    text not null,
  path       text not null,   -- percorso/identificativo nel tuo archivio
  key        int              -- tonalità originale della base (opzionale)
);

-- =========================
-- ENUM: stato scelta
-- =========================

do $$ begin
  create type scelta_status as enum ('queued','playing','done','skipped');
exception when duplicate_object then null; end $$;

-- =========================
-- TABELLA: Scelta (richiesta)
-- =========================

create table scelta (
  id_scelta      serial primary key,
  data_scelta    timestamptz not null default now(),
  status         scelta_status not null default 'queued',
  -- trasposizione in semitoni (-6..+6 consigliato a livello app)
  note           text,
  cantante_id    int not null references cantante(id) on delete cascade,
  canzone_id     int not null references canzone(id_canzone),
  sessione_id    int not null references sessione(id) on delete cascade
);

-- =========================
-- Indici minimi consigliati
-- =========================

create index idx_scelta_sessione_status on scelta (sessione_id, status, data_scelta);
create index idx_canzone_titolo on canzone (lower(titolo));
create index idx_canzone_artista on canzone (lower(artista));
