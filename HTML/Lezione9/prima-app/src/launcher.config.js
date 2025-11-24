import Stampanumeri from "./Esercizi/Esercizio1/Stampanumeri";
import Tabellina from "./Esercizi/Esercizio1/Tabellina";
import ProfiloUtenteDemo from "./Esercizi/Esercizio2/ProfiloUtenteDemo";
import Contatore from "./Esercizi/Esercizio3/Contatore";
import EsempioUseEffect from "./Esercizi/Esercizio4/EsempioUseEffect";
import CleanUp from "./Esercizi/Esercizio5/CleanUp";
import CambiaNome from "./Esercizi/Esercizio6/CambiaNome";
import Login from "./Esercizi/Esercizio7/Login";
import UserList from "./Esercizi/Esercizio8/UserList";
import Saluto from "./Esercizi/Esercizio9/Esercizio9_1/Saluto";
import CardUtenteDemo from "./Esercizi/Esercizio9/Esercizio9_2/CardUtenteDemo";
import MenuRistorante from "./Esercizi/Esercizio9/Esercizio9_3/MenuRistorante";
import Termostato from "./Esercizi/Esercizio9/Esercizio9_4/Termostato";
import CampoRicerca from "./Esercizi/Esercizio9/Esercizio9_5/CampoRicerca";
import MessaggioSegreto from "./Esercizi/Esercizio9/Esercizio9_6/MessaggioSegreto";
import AggiornaTitolo from "./Esercizi/Esercizio9/Esercizio9_7/AggiornaTitolo";
import GalleriaFoto from "./Esercizi/Esercizio9/Esercizio9_8/GalleriaFoto";
import ModuloContatti from "./Esercizi/Esercizio9/Esercizio9_9/ModuloContatti";
import BlogApp from "./Esercizi/Esercizio9/Esercizio9_10/BlogApp";
import TodoApp from "./Esercizi/Esercizio10/TodoApp";
import MostraNascondi from "./Esercizi/Esercizio11/Esercizio11_1/MostraNascondi";
import CambioColore from "./Esercizi/Esercizio11/Esercizio11_2/CambioColore";
import EchoInput from "./Esercizi/Esercizio11/Esercizio11_3/EchoInput";
import Pizza from "./Esercizi/Esercizio11/Esercizio11_4/Pizza";
import CheckboxMultiple from "./Esercizi/Esercizio12/CheckboxMultiple";
import MarcaModello from "./Esercizi/Esercizio13/MarcaModello";
import UtenteTarga from "./Esercizi/Esercizio14/UtenteTarga";

export const esercizi = [
  {
    titolo: "🔧 Esercizi Funzionali",
    items: [
      {
        nome: "Tabellina",
        path: "/esercizi/tabellina",
        componente: <Tabellina />,
      },
      {
        nome: "Contatore",
        path: "/esercizi/contatore",
        componente: <Contatore />,
      },
      {
        nome: "Profilo Utente",
        path: "/esercizi/profilo-utente",
        componente: <ProfiloUtenteDemo />,
      },
      {
        nome: "UserList",
        path: "/esercizi/UserList",
        componente: <UserList />,
      },
      {
        nome: "MostraNascondi",
        path: "/esercizi/esercizio11/esercizio11_1",
        componente: <MostraNascondi />,
      },
      {
        nome: "CambioColore",
        path: "/esercizi/esercizio11/esercizio11_2",
        componente: <CambioColore />,
      },
      {
        nome: "EchoInput",
        path: "/esercizi/esercizio11/esercizio11_3",
        componente: <EchoInput />,
      },
      {
        nome: "Pizza",
        path: "/esercizi/esercizio11/esercizio11_4",
        componente: <Pizza />,
      },
      {
        nome: "CheckboxMultiple",
        path: "/esercizi/esercizio12",
        componente: <CheckboxMultiple />,
      },
      {
        nome: "UtenteTarga",
        path: "/esercizi/esercizio14",
        componente: <UtenteTarga />,
      },
    ],
  },
  {
    titolo: "📘 Studio / Teoria",
    items: [
      {
        nome: "Stampa Numeri",
        path: "/esercizi/stampa-numeri",
        componente: <Stampanumeri />,
      },
      {
        nome: "UseEffect",
        path: "/esercizi/useEffect",
        componente: <EsempioUseEffect />,
      },
      { nome: "CleanUp", path: "/esercizi/CleanUp", componente: <CleanUp /> },
      {
        nome: "CambiaNome",
        path: "/esercizi/CambiaNome",
        componente: <CambiaNome />,
      },
      { nome: "Login", path: "/esercizi/Login", componente: <Login /> },
      {
        nome: "Saluto",
        path: "/esercizi/esercizio9/esercizio9_1",
        componente: <Saluto />,
      },
      {
        nome: "CardUtente",
        path: "/esercizi/esercizio9/esercizio9_2",
        componente: <CardUtenteDemo />,
      },
      {
        nome: "MenuRistorante",
        path: "/esercizi/esercizio9/esercizio9_3",
        componente: <MenuRistorante />,
      },
      {
        nome: "Termostato",
        path: "/esercizi/esercizio9/esercizio9_4",
        componente: <Termostato />,
      },
      {
        nome: "CampoRicerca",
        path: "/esercizi/esercizio9/esercizio9_5",
        componente: <CampoRicerca />,
      },
      {
        nome: "MessaggioSegreto",
        path: "/esercizi/esercizio9/esercizio9_6",
        componente: <MessaggioSegreto />,
      },
      {
        nome: "AggiornaTitolo",
        path: "/esercizi/esercizio9/esercizio9_7",
        componente: <AggiornaTitolo />,
      },
      {
        nome: "GalleriaFoto",
        path: "/esercizi/esercizio9/esercizio9_8",
        componente: <GalleriaFoto />,
      },
      {
        nome: "ModuloContatti",
        path: "/esercizi/esercizio9/esercizio9_9",
        componente: <ModuloContatti />,
      },
      {
        nome: "BlogApp",
        path: "/esercizi/esercizio9/esercizio9_10",
        componente: <BlogApp />,
      },
      { nome: "TodoApp", path: "/esercizi/TodoApp", componente: <TodoApp /> },
      {
        nome: "MarcaModello",
        path: "/esercizi/esercizio9/esercizio13",
        componente: <MarcaModello />,
      },
    ],
  },
];

export const raccolte = [
  {
    // Nome della card che vedrai in Home
    nome: "Esercizi Agosto",
    // Nuovo URL della pagina che mostrerà solo le 11 card
    path: "/raccolta1/esercitazione-react-11",
    // Metti qui i path dei 11 esercizi (quelli già definiti in `esercizi[].items[].path`)
    // Esempio (SOSTITUISCI con i tuoi 11):
    include: [
      "/esercizi/esercizio9/esercizio9_1",
      "/esercizi/esercizio9/esercizio9_2",
      "/esercizi/esercizio9/esercizio9_3",
      "/esercizi/esercizio9/esercizio9_4",
      "/esercizi/esercizio9/esercizio9_5",
      "/esercizi/esercizio9/esercizio9_6",
      "/esercizi/esercizio9/esercizio9_7",
      "/esercizi/esercizio9/esercizio9_8",
      "/esercizi/esercizio9/esercizio9_9",
      "/esercizi/esercizio9/esercizio9_10",
      "/esercizi/esercizio9/esercizio9_11",
    ],

    // true = nasconde questi figli dalla Home, mostrando al loro posto questa unica card
    hideChildrenFromHome: true,
  },
  {
    // Nome della card che vedrai in Home
    nome: "Esercizi UseState",
    // Nuovo URL della pagina che mostrerà solo le 4 card
    path: "/raccolta2/esercitazione-UseState-4",
    // Metti qui i path dei 4 esercizi (quelli già definiti in `esercizi[].items[].path`)
    // Esempio (SOSTITUISCI con i tuoi 4):
    include: [
      "/esercizi/esercizio11/esercizio11_1",
      "/esercizi/esercizio11/esercizio11_2",
      "/esercizi/esercizio11/esercizio11_3",
      "/esercizi/esercizio11/esercizio11_4",
    ],

    // true = nasconde questi figli dalla Home, mostrando al loro posto questa unica card
    hideChildrenFromHome: true,
  },
];
