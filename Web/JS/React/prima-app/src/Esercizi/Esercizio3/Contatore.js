import React, { useState } from 'react';

const Contatore = () => {

    const [count, setCount] = useState(0);

    const incrementa = () => setCount(count + 1)
    const decrementa = () => setCount(count - 1)

  return (

    <div>

        <h2>Contatore: {count}</h2>
        <button onClick={decrementa}>Decrementa</button>
        <button onClick={incrementa}>Incrementa</button>
        
    </div>

  )
}

export default Contatore