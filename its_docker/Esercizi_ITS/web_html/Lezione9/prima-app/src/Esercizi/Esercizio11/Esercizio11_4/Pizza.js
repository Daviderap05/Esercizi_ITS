import React, { useState } from 'react'

const Pizza = () => {
const [scelta, setScelta] = useState("");

  return (
    <div className='p-5'>
        
        <select 
          className="form-select" 
          aria-label="Default select example" 
          value={scelta} 
          onChange={(e) => setScelta(e.target.value)}
        >
            <option value="">Scegli una pizza</option>
            <option value="Margherita">Margherita</option>
            <option value="Capricciosa">Capricciosa</option>
            <option value="Diavola">Diavola</option>
            <option value="Boscaiola">Boscaiola</option>
        </select>

        <p style={{marginTop: "20px"}}>Hai scelto: {scelta}</p>

    </div>
  )
}

export default Pizza