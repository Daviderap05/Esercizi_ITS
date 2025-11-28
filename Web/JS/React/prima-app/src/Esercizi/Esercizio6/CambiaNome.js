import React, { useState } from 'react'

const CambiaNome = () => {

    const [nome, setNome] = useState("Roberto");

    const cambiaN = () => { 

        // if (nome === "Roberto"){
        //     setNome("Mario")

        // }else{
        //     setNome("Roberto")
        // }

        setNome(current => {
            if (current === "Roberto")
                return "Mario"
            return "Roberto";
        })
    }

  return (
    <div>

        <h2>Nome: {nome}</h2>
        <button class = "btn btn-dark" onClick={cambiaN}>Cambia</button>

    </div>
  )
}

export default CambiaNome