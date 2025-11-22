import React from 'react'
import { useState } from 'react'

const ModuloContatti = () => {

    const [info, setInfo] = useState({nome: '', email: '', messaggio: ''})

    const handleChange = (e) => {

        setInfo({

            ...info, [e.target.name]: e.target.value

        })
        
    }

  return (

    <div>
        
        Nome<input type='text' className='form-control' id='inputNome' name='nome' value={info.nome} onChange={handleChange}/>
        Email<input type='text' className='form-control' id='inputEmail' name='email' value={info.email} onChange={handleChange}/>

        Text Area<textarea className="form-control" id='inputMessaggio' name='messaggio' rows='10' value={info.messaggio} onChange={handleChange}/>

        <button type="button" className="btn btn-primary" onClick={() => console.log(info)}>Invia</button>

    </div>
  )
}

export default ModuloContatti