import React, { useEffect } from 'react'

export const EsempioUseEffect = () => {

    useEffect(() =>{

        console.log("sto usando useEffect")

    })

    console.log("Fuori dallo useEffect")

  return (
    <div>EsempioUseEffect</div>
  )
}

export default EsempioUseEffect;