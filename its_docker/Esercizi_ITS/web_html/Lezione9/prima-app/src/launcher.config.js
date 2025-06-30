import Stampanumeri from './Esercizi/Esercizio1/Stampanumeri';
import Tabellina from './Esercizi/Esercizio1/Tabellina';
import ProfiloUtenteDemo from './Esercizi/Esercizio2/ProfiloUtenteDemo';
import Contatore from './Esercizi/Esercizio3/Contatore';

export const esercizi = [
  { nome: 'Stampa Numeri', path: '/esercizi/stampa-numeri', componente: <Stampanumeri /> },
  { nome: 'Tabellina', path: '/esercizi/tabellina', componente: <Tabellina /> },
  { nome: 'Profilo Utente', path: '/esercizi/profilo-utente', componente: <ProfiloUtenteDemo /> },
  { nome: 'Contatore', path: '/esercizi/contatore', componente: <Contatore /> },  
];