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
    <div className="container">
      <h1 style={{ textAlign: "center", marginBottom: "24px" }}>
        Fetch Users, Albums e Photos
      </h1>
      <div
        style={{
          display: "flex",
          gap: "16px",
          flexWrap: "wrap",
          justifyContent: "center",
        }}
      >
        <select
          className="form-select"
          onChange={handleChange}
          value={userSelected}
          style={{ maxWidth: "400px" }}
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
          style={{ maxWidth: "400px" }}
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
      </div>

      <br></br>

      <ul
        style={{
          listStyle: "none",
          padding: 0,
          marginTop: "24px",
          maxWidth: "813px",
          marginInline: "auto",
        }}
      >
        {photos.map((u) => {
          return (
            <li
              key={u.id}
              style={{
                padding: "10px 14px",
                marginBottom: "16px",
                borderRadius: "8px",
                backgroundColor: "#f5f5f5",
                boxShadow: "0 2px 4px rgba(0,0,0,0.08)",
                fontSize: "14rm",
              }}
            >
              {u.title}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default FetchDemo;
