import React, { useEffect, useState } from "react";

const LoginDemo = () => {
  const URL =
    "https://login-11d88-default-rtdb.europe-west1.firebasedatabase.app/";

  const [email, setEmail] = useState("");
  const [psw, setPsw] = useState("");
    const [users, setUsers] = useState([]);
    
  async function getUsers() {
    try {
      let response = await fetch(URL + "loginAttempts" + ".json");

      if (!response.ok) {
        console.error("Errore: " + response.status);
      }

      let dati = await response.json();

      if (!dati) {
        return;
      }

      setUsers(Object.entries(dati));
    } catch (error) {
      console.error("Errore: " + error);
    }
    }
    
  async function invioForm(e) {
    e.preventDefault();
    try {
      const loginUser = { email: email, psw: psw };

      const response = await fetch(URL + "loginAttempts" + ".json", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(loginUser),
      });

      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }

      getUsers();
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useEffect(() => {
    getUsers();
  }, []);
  return (
    <>
      <div
        className="container"
        style={{ display: "flex", justifyContent: "center" }}
      >
        <form
          method="POST"
          name="login"
          onSubmit={invioForm}
          style={{ display: "flex", flexDirection: "column", width: "480px" }}
        >
          <label>Email:</label>
          <input
            type="text"
            placeholder="Inserisci Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ marginBottom: "16px" }}
          ></input>

          <label>Password:</label>
          <input
            type="password"
            placeholder="Inserisci Psw"
            value={psw}
            onChange={(e) => setPsw(e.target.value)}
            required
            style={{ marginBottom: "16px" }}
          ></input>

          <button
            type="submit"
            className="btn btn-primary"
            style={{ width: "80px", margin: "auto" }}
          >
            Invia
          </button>
        </form>
      </div>
      <ul>
        {users.map((u) => {
          return (
            <li key={u[0]}>
              EMAIL: {u[1].email} PASSWORD: {u[1].psw}
            </li>
          );
        })}
      </ul>
    </>
  );
};

export default LoginDemo;
