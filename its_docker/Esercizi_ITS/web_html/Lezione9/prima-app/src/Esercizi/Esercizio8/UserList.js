import React, { useEffect, useState } from 'react';

const url = "https://jsonplaceholder.typicode.com/users";

const UserList = () => {
  const [ users, setUsers ] = useState( [] );
  const [ selectedId, setSelectedId ] = useState( "" ); // valore della select

  const getData = async () => {
    try {
      const res = await fetch( url );
      const data = await res.json();
      setUsers( data );
    } catch ( error ) {
      console.error( "Errore nel caricamento utenti:", error );
    }
  };

  useEffect( () => {
    getData();
  }, [] );

  // Trova l'utente selezionato
  const selectedUser = users.find( user => user.id === parseInt( selectedId ) );

  return (
    <>
      <h1>Seleziona un utente</h1>

      <select value={ selectedId } onChange={ ( e ) => setSelectedId( e.target.value ) }>
        <option value="">-- Seleziona un nome --</option>
        {users.map( ( user ) => (
          <option key={ user.id } value={ user.id }>
            { user.name }
          </option>
        ) ) }
      </select>

      { selectedUser && (
        <div className="card shadow" style={ { marginTop: '1rem' } }>
          <img src={ `https://i.pravatar.cc/150?img=${selectedUser.id }`} alt={ selectedUser.name } />
          <h3>{ selectedUser.name }</h3>
          <p><strong>Email:</strong> { selectedUser.email }</p>
          <p><strong>Sito:</strong> <a href={ `https://${selectedUser.website}` } target="_blank">{ selectedUser.website }</a></p>
        </div>
      )}
    </>
  );
};

export default UserList;