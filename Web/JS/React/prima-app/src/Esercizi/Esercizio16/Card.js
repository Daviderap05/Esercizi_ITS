import React, { useState } from "react";
import styles from "./css/Card.module.css";

const Card = ({ theme }) => {
  const [isRed, setIsRed] = useState(false);

  function toggleTextColor() {
    setIsRed((v) => !v);
  }

  return (
    <div
      className={[
        styles.card,
        theme === "dark" ? styles.dark : styles.light,
        isRed ? styles.textRed : styles.textNormal,
      ].join(" ")}
      tabIndex={0}
      onClick={toggleTextColor}
    >
      <div className={styles.title}>
        <h2>Titolo</h2>
      </div>

      <div>
        <p>Contenuto</p>
      </div>
    </div>
  );
};

export default Card;
