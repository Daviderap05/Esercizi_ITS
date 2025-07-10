import React, { useEffect, useState } from 'react'
//mette a video la dimensione della finestra del browser
const CleanUp = () => {
    //console.log(window)

    const [size, setSize] = useState(window.innerWidth) // inizializza size alla largezza del video

    const dimensione = () => {
        setSize(window.innerWidth)
    }

    useEffect(() => {   //al render del componente aggiunge un evento su onresize che esegue dimensione
        window.addEventListener("resize", dimensione)
        return (() => {
            window.removeEventListener("resize", dimensione)
        })
    })
  return (
    <h1 >{size}</h1>
  )
}

export default CleanUp