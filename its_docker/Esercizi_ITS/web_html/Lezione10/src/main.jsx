import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import 'bootstrap/dist/css/bootstrap.css'
import UserAlbum from './UserAlbum.jsx'
import App from './App.jsx'



createRoot(document.getElementById('root')).render(
  <UserAlbum></UserAlbum>,
)
