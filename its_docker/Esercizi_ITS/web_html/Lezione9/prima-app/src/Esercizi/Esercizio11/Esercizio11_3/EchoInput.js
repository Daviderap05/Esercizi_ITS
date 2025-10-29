import React, { useState } from 'react'

const EchoInput = () => {
    const [testo, setTesto] = useState("");
  return (
    <div>
        
        <input className='form-control' onChange={(e) => setTesto(e.target.value)}></input>
        <br></br>
        <p>Hai scritto: {testo}</p>

    </div>
  )
}

export default EchoInput