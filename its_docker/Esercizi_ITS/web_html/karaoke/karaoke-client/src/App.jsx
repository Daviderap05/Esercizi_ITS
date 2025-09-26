import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";
import QRPage from "./pages/QRPage";
import AdminPage from "./pages/AdminPage";
import "./index.css";

export default function App() {
  return (
    <Router>
      <nav className="nav">
        <NavLink to="/" end>Home</NavLink>
        <NavLink to="/qr">Cantante</NavLink>
        <NavLink to="/admin">Admin</NavLink>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/qr" element={<QRPage />} />
          <Route path="/admin" element={<AdminPage />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home(){
  return (
    <div className="card">
      <h1 className="h1">Benvenuto al Karaoke</h1>
      <p className="note">Usa “Cantante” per inviare una richiesta, “Admin” per vedere la coda.</p>
    </div>
  );
}
