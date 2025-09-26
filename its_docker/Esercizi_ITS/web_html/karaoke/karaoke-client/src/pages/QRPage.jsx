import { useState } from "react";
import SongSearch from "../components/SongSearch";

export default function QRPage() {
  const [nome, setNome] = useState("");
  const [hasUsb, setHasUsb] = useState(false);
  const [semitoni, setSemitoni] = useState(0);
  const [note, setNote] = useState("");
  const [scelte, setScelte] = useState([]);

  const handleSongSelect = (song) => {
    if(!nome.trim()) { alert("Inserisci il tuo nome"); return; }
    const nuova = { cantante: nome.trim(), hasUsb, song, semitoni, note, ts: Date.now() };
    setScelte(prev => [nuova, ...prev]);
    setNote("");
  };

  return (
    <div className="grid">
      <div className="card">
        <h1 className="h1">Invia richiesta</h1>
        <div className="grid">
          <input className="input" placeholder="Il tuo nome"
                 value={nome} onChange={(e)=>setNome(e.target.value)} />
          <div className="row">
            <label className="checkbox">
              <input type="checkbox" checked={hasUsb} onChange={e=>setHasUsb(e.target.checked)} />
              Ho una chiavetta USB
            </label>
            <span className="badge">{hasUsb ? "USB" : "No USB"}</span>
          </div>

          <div className="card" style={{padding:14}}>
            <div className="row" style={{justifyContent:"space-between"}}>
              <strong>Tonalità</strong>
              <span className="small">{semitoni} semitoni</span>
            </div>
            <input className="slider" type="range" min={-6} max={6}
                   value={semitoni} onChange={(e)=>setSemitoni(parseInt(e.target.value))}/>
            <p className="note">-2 = più bassa · +2 = più alta</p>
          </div>

          <input className="input" placeholder="Note (opzionale)"
                 value={note} onChange={(e)=>setNote(e.target.value)} />

          <SongSearch onSelect={handleSongSelect} />
        </div>
      </div>

      <div className="card">
        <h2 className="h1">Le tue richieste</h2>
        <ul className="list">
          {scelte.length === 0 && <p className="note">Ancora nessuna richiesta.</p>}
          {scelte.map((s,i)=>(
            <li key={s.ts+i} className="item">
              <div className="meta">
                <strong>{s.song.titolo}</strong>
                <span className="small">{s.song.artista} · {s.semitoni>=0?`+${s.semitoni}`:s.semitoni} st · {s.hasUsb?"USB":"no USB"}</span>
              </div>
              <span className="badge">{s.cantante}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
