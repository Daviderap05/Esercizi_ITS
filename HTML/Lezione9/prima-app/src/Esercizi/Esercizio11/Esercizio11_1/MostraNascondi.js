import {React, useState} from 'react'

const MostraNascondi = () => {
  const [state, setState] = useState(false);
  return (
    <div>
      
      <button className='btn btn-primary m-2' onClick={() => setState(!state)}>{state ? "Nascondi" : "Mostra"}</button>
      {state && <p>Mostrato</p>}  {/* --> && se true fai quello ... */}

    </div>
  )
}

export default MostraNascondi