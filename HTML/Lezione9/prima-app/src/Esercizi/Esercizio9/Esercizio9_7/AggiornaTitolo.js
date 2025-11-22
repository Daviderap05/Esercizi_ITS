import React from 'react'
import { useState, useEffect} from 'react'

const AggiornaTitolo = () => {

    const [nome, setNome] = useState('');

    useEffect(() => {
        if (nome === '') {
            document.title = "Benvenuto!";
        } else {
            document.title = `Ciao, ${nome}!`;
        }
    }, [nome]);

  return (
    <div>
        <input type="text" className='form-control' id='inputTesto' onChange={e => setNome(e.target.value)}/>
    </div>
  )
}

export default AggiornaTitolo