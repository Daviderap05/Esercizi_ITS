import React, { useState, useRoutes } from 'react'
import  { BrowserRouter, Route, Routes, Link } from 'react-router-dom'
import Home from './Home'
import About from './About'
import Profiles from './Profiles'
import ErrorPage from './ErrorPage'
import SingleProfile from './SingleProfile'
import MyProfile from './MyProfile'
import { routes } from './routes'

const AppRoutes = () =>{
    const element = useRoutes(routes)
      return element
    
}
const ProvaRouter = () => {

  // const [link, setLink] = useState("Home")
  // const handleRender = () => {

  //   if (link === "Home"){

  //     return <Home></Home>

  //   }

  //   if (link === "About"){

  //     return <About></About>

  //   }

  //   if (link === "Profiles"){

  //     return <Profiles></Profiles>

  //   }
  // }

  return (
    <div className='container-md'>

        <BrowserRouter>

          <nav className='navbar'>

            <Link to='/'>Home</Link>
            <Link to='/about'>About</Link>
            <Link to='/profiles'>Profiles</Link>
            
          </nav>

          <hr></hr>

          <AppRoutes></AppRoutes>
          {/* <Routes>
          
            <Route path='/' element={<Home></Home>}></Route>
            <Route path='/about' element={<About></About>}></Route>
            <Route path='/profiles' element={<Profiles></Profiles>}></Route>
              <Route path='/profiles/:id' element={<SingleProfile></SingleProfile>}>
              <Route path='/profiles/me' element={<MyProfile></MyProfile>}></Route>
            </Route>
            <Route path='*' element={<ErrorPage></ErrorPage>}></Route>

          </Routes> */}

        </BrowserRouter>
        
        {/* <nav className='navbar'>

            <button className='btn btn-link nav-link' onClick={() => setLink("Home")}>Home</button>
            <button className='btn btn-link nav-link' onClick={() => setLink("About")}>About</button>
            <button className='btn btn-link nav-link' onClick={() => setLink("Profiles")}>Profiles</button>

        </nav>

        <div>

            {handleRender()}

        </div> */}

    </div>
  )
}

export default ProvaRouter