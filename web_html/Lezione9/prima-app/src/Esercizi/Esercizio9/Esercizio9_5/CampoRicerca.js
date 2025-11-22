import React from 'react'
import { useState } from 'react'

const CampoRicerca = () => {

    const [testoRicerca, setTesto] = useState('')

    return (
        <div>
            
            <input type="text" value={testoRicerca}  className='form-control' id='inputTesto' onChange={e => setTesto(e.target.value)}/>
            <p style={{ marginTop: '15px' }}>Stai cercando: {testoRicerca}</p>
            
        </div>
    )
}

export default CampoRicerca