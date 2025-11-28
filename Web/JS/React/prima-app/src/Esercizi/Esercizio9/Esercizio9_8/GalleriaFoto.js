import React, { useState, useEffect } from 'react'

const GalleriaFoto = () => {

  const [foto, setFoto] = useState([])
  const [staCaricando, setStaCaricando] = useState(true)
  const [errore, setErrore] = useState(null)

  useEffect(() => {

    const fetchFoto = async () => {

      try {

        const res = await fetch('https://jsonplaceholder.typicode.com/photos?_limit=10')
        const data = await res.json()
        setFoto(data)
        setStaCaricando(false)

      } catch (err) {

        setErrore(err.message)
        setStaCaricando(false)

      }

    }

    fetchFoto()

  }, [])

  return (

    <div>

      <h2>Galleria Foto</h2>

      <div>

        {foto.map(f => (

          <div key={f.id} style={{width: '120px'}}>

            <img src={f.thumbnailUrl} alt={f.title} style={{width: '100%'}} />
            <p>{f.title}</p>

          </div>

        ))}

      </div>

    </div>

  )
}

export default GalleriaFoto