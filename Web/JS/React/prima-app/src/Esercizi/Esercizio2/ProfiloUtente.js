import React from 'react';

const ProfiloUtente = ({ utente }) => {

  const mostraDettagli = () => {

    alert(`Dettagli Utente:

      Nome: ${utente.nome}
      Cognome: ${utente.cognome}
      Età: ${utente.eta}
      Professione: ${utente.professione}
      Email: ${utente.email}`);

  };

  return (

    <div className="card h-100">

      <div className="card-header text-center"> 

        <h5>{utente.nome} {utente.cognome}</h5>

      </div>

      <div className="card-body text-center">

        <p><span className="badge bg-primary">Età: {utente.eta}</span></p>
        <p>Professione: {utente.professione}</p>
        <p>Email: {utente.email}</p>

      </div>

      <div className="card-footer text-center">

        <button className="btn btn-outline-info btn-sm" onClick={mostraDettagli}>
          
          Mostra dettagli

        </button>

      </div>

    </div>

  );

};

export default ProfiloUtente;