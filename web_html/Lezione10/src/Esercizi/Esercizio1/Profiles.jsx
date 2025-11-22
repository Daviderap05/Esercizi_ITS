import React from 'react'
import { Link, Outlet} from 'react-router-dom'

const Profiles = () => {
  return (

    <>
    
      <div>Pagina Profiles</div>
      <hr></hr>

      <nav className='navbar'>

        <Link to="me">My profile</Link>
        <Link to="2">Single profile con id 2</Link>

      </nav>

      <div><Outlet></Outlet></div>
    
    </>
  )
}

export default Profiles