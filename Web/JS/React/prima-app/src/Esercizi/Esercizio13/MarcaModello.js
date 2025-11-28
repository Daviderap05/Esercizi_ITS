import { useState } from "react";
import React from "react";
import modelliPerMarca from "../../dati/marcaModello";
const MarcaModello = () => {
  const [marca, setMarca] = useState("");
  const modelli = marca ? modelliPerMarca[marca] : [];

  return (
    <>
      <div class="container mt-5">
        <div class="row mb-3">
          <div class="col">
            <label for="marca" class="form-label">
              Seleziona la marca:
            </label>
            <select
              id="marca"
              name="marca"
              class="form-select"
              value={marca}
              onChange={(e) => setMarca(e.target.value)}
            >
              <option value="">Seleziona marca</option>
              <option value="bmw">BMW</option>
              <option value="mercedes">Mercedes</option>
              <option value="audi">Audi</option>
            </select>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <label for="modello" class="form-label">
              Seleziona il modello:
            </label>
            <select id="modello" name="modello" class="form-select" disabled = {!marca}>
              <option value="">Seleziona modello</option>
              {modelli.map((modello) => {
                return <option value={modello}>{modello}</option>;
              })}
            </select>
          </div>
        </div>
      </div>
    </>
  );
};

export default MarcaModello;
