import Stampanumeri from './Esercizi/Esercizio1/Stampanumeri';
import Tabellina from './Esercizi/Esercizio1/Tabellina';
import ProfiloUtenteDemo from './Esercizi/Esercizio2/ProfiloUtenteDemo';
import Contatore from './Esercizi/Esercizio3/Contatore';
import EsempioUseEffect from './Esercizi/Esercizio4/EsempioUseEffect';
import CleanUp from './Esercizi/Esercizio5/CleanUp';

export const esercizi = [
  {
    titolo: '🔧 Esercizi Funzionali',
    items: [
      { nome: 'Stampa Numeri', path: '/esercizi/stampa-numeri', componente: <Stampanumeri /> },
      { nome: 'Tabellina', path: '/esercizi/tabellina', componente: <Tabellina /> },
      { nome: 'Contatore', path: '/esercizi/contatore', componente: <Contatore /> },
    ]
  },
  {
    titolo: '📘 Studio / Teoria',
    items: [
      { nome: 'Profilo Utente', path: '/esercizi/profilo-utente', componente: <ProfiloUtenteDemo /> },
      { nome: 'UseEffect', path: '/esercizi/useEffect', componente: <EsempioUseEffect /> },
      { nome: 'CleanUp', path: '/esercizi/CleanUp', componente: <CleanUp /> }
    ]
  }
];