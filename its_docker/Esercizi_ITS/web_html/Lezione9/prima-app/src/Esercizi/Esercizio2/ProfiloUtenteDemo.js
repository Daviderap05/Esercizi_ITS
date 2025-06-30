import React from 'react';
import ProfiloUtente from './ProfiloUtente';

const utenti = [
  { id: 1, nome: 'Davide', cognome: 'Raponi', eta: 18, professione: 'Studente', email: 'davide@email.com' },
  { id: 2, nome: 'Anna', cognome: 'Rossi', eta: 25, professione: 'Designer', email: 'anna@email.com' },
  { id: 3, nome: 'Luca', cognome: 'Bianchi', eta: 30, professione: 'Ingegnere', email: 'luca@email.com' },
  { id: 4, nome: 'Maria', cognome: 'Verdi', eta: 27, professione: 'Medico', email: 'maria@email.com' },
  { id: 5, nome: 'Marco', cognome: 'Neri', eta: 33, professione: 'Avvocato', email: 'marco@email.com' },
  { id: 6, nome: 'Elisa', cognome: 'Gialli', eta: 22, professione: 'Sviluppatrice', email: 'elisa@email.com' },
];

const ProfiloUtenteDemo = () => {

  const raggruppaInTre = (array) => {

    const gruppi = [];

    for (let i = 0; i < array.length; i += 3) {

      gruppi.push(array.slice(i, i + 3));

    }

    return gruppi;

  };

  const righe = raggruppaInTre(utenti);

  return (

    <div className="container mt-3">

      {righe.map((gruppo, index) => (

        <div className="row mb-4" key={index}>

          {gruppo.map((utente) => (

            <div className="col-md-4" key={utente.id}>

              <ProfiloUtente utente={utente} />

            </div>

          ))}

        </div>

      ))}

    </div>

  );
  
};

export default ProfiloUtenteDemo;