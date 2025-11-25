// App.js
import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useLocation,
} from "react-router-dom";
import { esercizi } from "./launcher.config";
import { raccolte as raccolteConfig } from "./launcher.config"; // import normale
import "./App.css";
const raccolte = raccolteConfig || [];

// Mappa path -> item esercizio (per recuperare componenti/titoli dai path)
function buildItemIndex() {
  const byPath = new Map();
  esercizi.forEach((gruppo) => {
    gruppo.items.forEach((item) => {
      byPath.set(item.path, item);
    });
  });
  return byPath;
}

// Un set con tutti i path inclusi in tutte le raccolte (per filtrarli dalla Home)
function buildIncludedPathsSet(raccolteArr) {
  const s = new Set();
  raccolteArr?.forEach((r) => (r.include || []).forEach((p) => s.add(p)));
  return s;
}

function PageHeader({ title, subtitle }) {
  return (
    <div className="text-center mb-5">
      <h1 className="fw-bold display-4">{title}</h1>
      {subtitle && <p className="text-muted">{subtitle}</p>}
    </div>
  );
}

function ExerciseCard({ title, to }) {
  return (
    <div className="col-12 col-sm-6 col-lg-4 mb-4">
      <Link to={to} className="text-decoration-none">
        <div className="card shadow-sm border-0 h-100 transition rounded-4">
          <div
            className="card-body d-flex align-items-center justify-content-center"
            style={{ minHeight: 120 }}
          >
            <h5 className="card-title fw-bold m-0 text-center">{title}</h5>
          </div>
          <div className="card-footer bg-transparent text-center">
            <span className="btn btn-sm">Apri</span>
          </div>
        </div>
      </Link>
    </div>
  );
}

function Section({ title, children }) {
  if (!children) return null;
  return (
    <div className="mb-5">
      <h2 className="h4 fw-bold mb-3">{title}</h2>
      <div className="row">{children}</div>
    </div>
  );
}

// HOME: come prima, ma nascondiamo gli item che appartengono a raccolte (se hideChildrenFromHome)
function Home() {
  const [isDark, setIsDark] = React.useState(false);

  const toggleTheme = () => {
    setIsDark((prev) => {
      const next = !prev;
      document.body.classList.toggle("dark", next);
      return next;
    });
  };

  const byPath = buildItemIndex();
  const includedPaths = buildIncludedPathsSet(
    raccolte.filter((r) => r.hideChildrenFromHome)
  );

  return (
    <div className="container mt-5">
      {/* Pulsante minimal in alto a destra */}
      <div className="text-end mb-3">
        <button
          className="theme-toggle-btn rounded-pill px-3 py-2"
          onClick={toggleTheme}
        >
          {isDark ? "☀️" : "🌙"}
        </button>
      </div>

      <PageHeader
        title="🚀 React Playground"
        subtitle="Scegli un esercizio e inizia a sperimentare"
      />

      {/* Sezioni originali */}
      {esercizi.map((gruppo, gIndex) => {
        const visibleItems = gruppo.items.filter(
          (it) => !includedPaths.has(it.path)
        );
        if (visibleItems.length === 0) return null;
        return (
          <Section key={gIndex} title={gruppo.titolo}>
            {visibleItems.map((es, idx) => (
              <ExerciseCard key={idx} title={es.nome} to={es.path} />
            ))}
          </Section>
        );
      })}

      {/* Sezione Raccolte (solo se esistono) */}
      {Array.isArray(raccolte) && raccolte.length > 0 && (
        <Section title="📂 Raccolte">
          {raccolte.map((r, i) => (
            <ExerciseCard
              key={i}
              title={`${r.nome}${
                r.include?.length ? ` (${r.include.length})` : ""
              }`}
              to={r.path}
            />
          ))}
        </Section>
      )}
    </div>
  );
}

// HUB Raccolta: mostra solo le card dei figli inclusi, con lo stesso stile della Home
function CollectionHub({ raccolta }) {
  const byPath = buildItemIndex();
  const items = (raccolta.include || [])
    .map((p) => byPath.get(p))
    .filter(Boolean);

  return (
    <div className="container mt-5">
      <PageHeader
        title={raccolta.nome}
        subtitle={
          items.length
            ? `Seleziona uno dei ${items.length} esercizi`
            : "Nessun esercizio configurato"
        }
      />
      <div className="row">
        {items.map((es, idx) => (
          <ExerciseCard key={idx} title={es.nome} to={es.path} />
        ))}
      </div>

      <div className="mt-4">
        <Link to="/" className="btn btn-sm">
          {"← Torna alla Home"}
        </Link>
      </div>
    </div>
  );
}

function CollectionRouter() {
  const location = useLocation();

  // Trova quale raccolta corrisponde al path corrente
  const raccolta = (raccolte || []).find((r) => r.path === location.pathname);
  if (!raccolta) return <p className="container mt-4">Raccolta non trovata.</p>;

  return <CollectionHub raccolta={raccolta} />;
}

export default function App() {
  // Costruiamo anche tutte le route degli esercizi (immutate)
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />

        {/* Route per ogni esercizio (rimangono identiche) */}
        {esercizi.map((gruppo, gIdx) =>
          gruppo.items.map((es, idx) => (
            <Route
              key={`${gIdx}-${idx}`}
              path={es.path}
              element={es.componente}
            />
          ))
        )}

        {/* Route per ogni raccolta: mostra la pagina con le 11 card */}
        {Array.isArray(raccolte) &&
          raccolte.map((r, i) => (
            <Route
              key={`raccolta-${i}`}
              path={r.path}
              element={<CollectionRouter />}
            />
          ))}

        <Route
          path="*"
          element={<p className="container mt-4">Pagina non trovata.</p>}
        />
      </Routes>
    </Router>
  );
}
