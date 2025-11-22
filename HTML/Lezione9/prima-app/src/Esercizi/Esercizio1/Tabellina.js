import React, { useState } from 'react';

const Tabellina = () => {
  const [numero, setNumero] = useState('');
  const [moltiplicatore, setMoltiplicatore] = useState(null);

  const tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  const generaTabellina = (e) => {
    e.preventDefault();
    const num = parseInt(numero);
    if (!isNaN(num)) {
      setMoltiplicatore(num);
    }
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Generatore di Tabelline</h2>

      <form onSubmit={generaTabellina} className="mb-4">
        <div className="input-group">
          <input
            type="number"
            value={numero}
            onChange={(e) => setNumero(e.target.value)}
            className="form-control"
            placeholder="Inserisci un numero intero"
            required
          />
          <button type="submit" className="btn btn-primary">Genera</button>
        </div>
      </form>

      {moltiplicatore !== null && (
        <>
          <h4 className="mb-3">Tabellina del {moltiplicatore}</h4>
          {tab.map((n, i) => (
            <p key={i}>{n} × {moltiplicatore} = {n * moltiplicatore}</p>
          ))}
        </>
      )}
    </div>
  );
};

export default Tabellina;