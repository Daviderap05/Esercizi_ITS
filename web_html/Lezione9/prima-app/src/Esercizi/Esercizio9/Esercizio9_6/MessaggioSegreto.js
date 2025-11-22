import React, { useState } from 'react'

const MessaggioSegreto = () => {
  const [mostra, setMostra] = useState(false)

  return (
    <div>

      <button type="button" className="btn btn-primary" style={{marginBottom: '15px'}} onClick={() => setMostra(prev => !prev)}>
            {mostra ? 'Nascondi' : 'Mostra'}
      </button>
      
      {mostra && <p>Questo è il messaggio segreto!</p>}
      
    </div>
  )
}

export default MessaggioSegreto