import React, { useState, useEffect } from "react";
import skills from "../../dati/skills";

const CheckboxMultiple = () => {
  const [array, setArray] = useState([]);
  const [ultimaAzione, setUltimaAzione] = useState(false);

  const handleChange = (e) => {
    if (e.target.checked) {
      setUltimaAzione(true);
      setArray((prev) => [...prev, e.target.id]);
    } else {
      setUltimaAzione(false);
      setArray((prev) => prev.filter((item) => item !== e.target.id));
    }
  };

  const handleReset = () => {
    setArray([]);
    setUltimaAzione(false);
  };

  useEffect(() => {
    if (array.length === 6 && ultimaAzione) {
      alert("Hai superato le 5 selezioni");
    }
  }, [array]);

  return (
    <>
      <form onReset={handleReset}>
        <h1>Seleziona le skills:</h1>
        <br />

        <div style={{ marginBottom: "20px" }}>
          {skills.map((skill) => (
            <div className="form-check" key={skill.id}>
              <input
                id={String(skill.id)}
                className="form-check-input"
                type="checkbox"
                onChange={handleChange}
                checked={array.includes(String(skill.id))}
              />
              <label className="form-check-label">{skill.name}</label>
            </div>
          ))}

          <button
            className="btn btn-danger"
            type="reset"
            style={{ marginTop: "15px" }}
          >
            Resetta
          </button>
        </div>
      </form>

      <p>
        Numero di scelte:{" "}
        <span style={{ color: array.length < 6 ? "black" : "red" }}>
          {array.length}
        </span>{" "}
        / 10
      </p>

      <br></br>
      <h3>Skill selezionate:</h3>
      {array.map((id) => {
        const skill = skills.find((s) => String(s.id) === id);
        return <li key={id}>{skill.name}</li>;
      })}
    </>
  );
};

export default CheckboxMultiple;
