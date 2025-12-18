import React, { useState } from "react";
import styles from "./css/CardDemo.module.css";
import Card from "./Card";

const CardDemo = () => {
  const [theme, setTheme] = useState("light"); // "light" | "dark"

  function switchMode() {
    setTheme((t) => (t === "light" ? "dark" : "light"));
  }

  return (
    <div
      className={[
        styles.page,
        theme === "dark" ? styles.pageDark : styles.pageLight,
      ].join(" ")}
    >
      <div className={styles.topbar}>
        <button id="bottone" onClick={switchMode}>
          Cambia colore
        </button>
      </div>

      <div className={styles.grid}>
        <Card theme={theme} />
        <Card theme={theme} />
        <Card theme={theme} />
        <Card theme={theme} />
        <Card theme={theme} />
        <Card theme={theme} />
      </div>
    </div>
  );
};

export default CardDemo;
