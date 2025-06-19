import React from 'react';
import './App.css';
import Componente1 from './Componente1';
import Clock from './Clock';
import { anagrafica } from './dati/dati'; 
import Stampanumeri from './Esercizi/Stampanumeri';
import Tabellina from './Esercizi/Tabellina';

function getDate(date){
  return date.toLocaleDateString() + " " + date.toLocaleTimeString()
}
function App() {
  let nome = "Davide  ";
  return (
      <div className="App">

        <h1>Prima app React! {nome}</h1>

        <Componente1>pippo</Componente1>
        <Componente1/>
        <h2>

          {

            new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString() // mostra data e ora corrente

          }

        </h2>

        <h3>Data e ora corrente: {getDate(new Date())}</h3>
        <Clock timezone="0" country="ITALY"></Clock>
        <Clock timezone="18" country="USA"></Clock>
        <Clock timezone="7" country="JAPAN"></Clock>

        {
          anagrafica.map((p)=>{
            return  <Componente1 key={p.id} {...p}/>

          })
        }

        <Stampanumeri/>

        <Tabellina moltiplicatore={2}/>

      </div>
  );
}

export default App;