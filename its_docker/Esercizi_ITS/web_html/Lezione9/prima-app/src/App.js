import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { esercizi } from './launcher.config';

function Home() {
  return (
    <div className="container mt-5">
      <div className="text-center mb-4">
        <h1 className="fw-bold display-5">📘 Esercizi React</h1>
        <p className="text-muted">Scegli un esercizio da eseguire</p>
      </div>

      <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 justify-content-center">
        {esercizi.map((es, index) => (
          <div className="col" key={index}>
            <Link to={es.path} className="text-decoration-none">
              <div className="card shadow-sm border-0 h-100">
                <div className="card-body text-center">
                  <h5 className="card-title text-dark">{es.nome}</h5>
                </div>
                <div className="card-footer bg-transparent text-center">
                  <span className="btn btn-sm btn-outline-primary">Apri</span>
                </div>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        {esercizi.map((es, index) => (
          <Route key={index} path={es.path} element={es.componente} />
        ))}
        <Route path="*" element={<p className="container mt-4">Pagina non trovata.</p>} />
      </Routes>
    </Router>
  );
}

export default App;