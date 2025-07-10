// App.js aggiornato - Rimosso il cambio tema
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { esercizi } from './launcher.config';
import './App.css';

function Home() {
  return (
    <div className="container mt-5">
      <div className="text-center mb-5">
        <h1 className="fw-bold display-4">🚀 React Playground</h1>
        <p className="text-muted">Scegli un esercizio e inizia a sperimentare</p>
      </div>

      {esercizi.map((gruppo, gIndex) => (
        <div key={gIndex} className="mb-5">
          <h3 className={`text-${gruppo.colore} fw-semibold mb-3`}>{gruppo.titolo}</h3>

          <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
            {gruppo.items.map((es, index) => (
              <div className="col" key={index}>
                <Link to={es.path} className="text-decoration-none">
                  <div className="card shadow-sm border-0 h-100 transition rounded-4">
                    <div className="card-body text-center">
                      <h5 className="card-title fw-bold">{es.nome}</h5>
                    </div>
                    <div className="card-footer bg-transparent text-center">
                      <span className="btn btn-sm">Apri</span>
                    </div>
                  </div>
                </Link>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        {esercizi.map((gruppo) =>
          gruppo.items.map((es, index) => (
            <Route key={index} path={es.path} element={es.componente} />
          ))
        )}
        <Route path="*" element={<p className="container mt-4">Pagina non trovata.</p>} />
      </Routes>
    </Router>
  );
}

export default App;