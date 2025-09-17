import React from 'react'
import { useState } from 'react'

const Termostato = () => {

  const temperatura = 26;
  const [temp, setTemp] = useState(temperatura)

  const decrementa = () => {
  
    if (temp > -273){
      setTemp(temp - 1)
    }

  }
  
  const incrementa = () => setTemp(temp + 1)

  return (
    <div>
      
      <h1>La temperatura è di: {temp}°</h1>

      <button type="button" class="btn btn-primary" style={{ marginRight: '10px' }} onClick={decrementa}>Decrementa</button>
      <button type="button" class="btn btn-primary" onClick={incrementa}>Incrementa</button>
      
    </div>
  )
}

export default Termostato