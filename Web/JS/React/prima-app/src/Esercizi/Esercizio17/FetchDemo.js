import React, { useState, useEffect } from "react";

const FetchDemo = () => {
  const urlUsers = "https://jsonplaceholder.typicode.com/users";
  const urlAlbums = "https://jsonplaceholder.typicode.com/albums";
  const urlPhotos = "https://jsonplaceholder.typicode.com/photos";

  const [users, setUsers] = useState([]);
  const [userSelected, setUserSelected] = useState("");

  const [albums, setAlbums] = useState([]);
  const [albumSelected, setAlbumSelected] = useState("");

  const [photos, setPhotos] = useState([]);

  async function fetchUsers() {
    try {
      let response = await fetch(urlUsers);
      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }
      let dati = await response.json();
      setUsers(dati);
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useEffect(() => {
    fetchUsers();
  }, []);

  async function fetchAlbums(id) {
    const url = urlAlbums + "?userId=" + id;
    try {
      let response = await fetch(url);
      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }
      let dati = await response.json();
      setAlbums(dati);
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useEffect(() => {
    fetchAlbums(userSelected);
  }, [userSelected]);

  async function fetchPhotos(id) {
    const url = urlPhotos + "?albumId=" + id;
    try {
      let response = await fetch(url);
      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }
      let dati = await response.json();
      setPhotos(dati);
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useEffect(() => {
    fetchPhotos(albumSelected);
  }, [albumSelected]);

  function handleChange(e) {
    setUserSelected(e.target.value);
    setAlbums([]);
    setPhotos([]);
  }

  return (
    <div>
      <h1>Fetch Users, Albums e Photos</h1>
      <select
        className="form-select"
        onChange={handleChange}
        value={userSelected}
      >
        <option value="">Seleziona Utente</option>
        {users.map((u) => {
          return (
            <option key={u.id} value={u.id}>
              {u.name}
            </option>
          );
        })}
      </select>

      <select
        className="form-select"
        onChange={(e) => setAlbumSelected(e.target.value)}
        value={albumSelected}
        disabled={!userSelected}
      >
        <option value="">Seleziona Album</option>
        {albums.map((a) => {
          return (
            <option key={a.id} value={a.id}>
              {a.title}
            </option>
          );
        })}
      </select>

      <br></br>

      <ul>
        {photos.map((u) => {
          return (
            <li key={u.id} value={u.id}>
              {u.title}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default FetchDemo;
