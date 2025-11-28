import { useState } from "react";
import React from "react";

const UtenteTarga = () => {
  const [utente, setUtente] = useState("");
  const [targa, setTarga] = useState("");
  const [info, setInfo] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();

    const targaValida = /^[A-Z]{2}\d{3}[A-Z]{2}$/i.test(targa);

    const esisteGia = info.some((item) => item.targa === targa);

    if (targaValida && !esisteGia) {
      setInfo((prev) => [...prev, { utente, targa }]);
      setUtente("");
      setTarga("");
    } else {
      alert("Errore: targa non valida o già presente.");
    }
  };

  return (
    <>
      <div className="d-flex justify-content-center mt-4">
        <div
          className="card shadow-sm"
          style={{ maxWidth: "900px", width: "100%" }}
        >
          <div className="card-header bg-primary text-white fw-bold text-center">
            Elenco Utenti Registrati
          </div>

          <div className="table-responsive">
            <table className="table table-hover mb-0">
              <thead className="table-light">
                <tr className="text-center">
                  <th>Nome</th>
                  <th>Targa</th>
                </tr>
              </thead>

              <tbody className="text-center">
                {info.map((item, index) => (
                  <tr key={index}>
                    <td>{item.utente}</td>
                    <td>{item.targa}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <form className="row g-3">
        {/* Contenitore centrale */}
        <div className="col-12 d-flex justify-content-center">
          <div className="w-100" style={{ maxWidth: "500px" }}>
            {/* Nome */}
            <label htmlFor="inputNome" className="form-label"></label>
            <input
              type="text"
              value={utente}
              onChange={(e) => setUtente(e.target.value)}
              className="form-control mb-3"
              id="inputNome"
              placeholder="Nome e Cognome"
              required
            />

            {/* Targa */}
            <label htmlFor="inputTarga" className="form-label"></label>
            <input
              type="text"
              value={targa}
              onChange={(p) => setTarga(p.target.value.toUpperCase())}
              className="form-control"
              id="inputTarga"
              placeholder="Targa"
              required
            />
          </div>
        </div>

        {/* Bottone centrato */}
        <div className="col-12 d-flex justify-content-center">
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            Crea Account
          </button>
        </div>
      </form>
    </>
  );
};

export default UtenteTarga;
