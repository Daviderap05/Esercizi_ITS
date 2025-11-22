import { useMemo, useState } from "react";

const mockSongs = [
  { id: 1, titolo: "Volare", artista: "Domenico Modugno" },
  { id: 2, titolo: "Viva la vida", artista: "Coldplay" },
  { id: 3, titolo: "A te", artista: "Jovanotti" },
];

export default function SongSearch({ onSelect }) {
  const [q, setQ] = useState("");

  const results = useMemo(()=>{
    const s = q.trim().toLowerCase();
    if(!s) return mockSongs;
    return mockSongs.filter(x =>
      x.titolo.toLowerCase().includes(s) || x.artista.toLowerCase().includes(s)
    );
  },[q]);

  return (
    <div className="grid">
      <input className="input" placeholder="Cerca titolo o artista…"
             value={q} onChange={e=>setQ(e.target.value)} />
      <ul className="list">
        {results.map(r=>(
          <li key={r.id} className="item" onClick={()=>onSelect(r)} style={{cursor:"pointer"}}>
            <div className="meta">
              <strong>{r.titolo}</strong>
              <span className="small">{r.artista}</span>
            </div>
            <button className="button">Scegli</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
