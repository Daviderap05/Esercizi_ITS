import {React, useState} from 'react'

const CambioColore = () => {
    const [colore, setColore] = useState("black");
  return (
    <div>
        
        <h1 style={{textAlign: "center", color: colore, marginBottom: "1px"}}>Ciao Mondo!</h1>
        <p style={{textAlign: "center", color: "black", marginBottom: "40px"}}>Clicca i bottoni per cambiare il colore del titolo</p>

        {/* flex mette gli elementi uno a fianco l'altro */}
        <div style={{display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
            <button type="button" className="btn btn-danger" onClick={() => setColore("red")}>Rosso</button>
            <button type="button" className="btn btn-success" onClick={() => setColore("green")}>Verde</button>
            <button type="button" className="btn btn-primary" onClick={() => setColore("blue")}>Blu</button>
        </div>

    </div>
  )
}

export default CambioColore