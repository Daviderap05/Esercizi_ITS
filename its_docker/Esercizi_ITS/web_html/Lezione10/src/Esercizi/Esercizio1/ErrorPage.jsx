import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom';

const ErrorPage = () => {

    const navigate = useNavigate()

  return (
    <>

        <h2><center>Pagina non trovata</center></h2>
        <p><button className='btn btn-success' onClick={() => navigate('/')}>Torna alla Home</button></p>
        <p><button className='btn btn-primary' onClick={() => navigate(-1)}>Torna alla pagina precedente</button></p>
    </>
  )
}

export default ErrorPage;