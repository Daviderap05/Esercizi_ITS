// libri.js
import { URL_BASE } from "./config.js";
import { Libro } from "./models/Libro.js";
import { listaOggetti } from "./utils.js";

const URL_LIBRI = URL_BASE + "libri";

let dt = null; // riferimento DataTable

async function leggiLibri() {
  try {
    const response = await fetch(URL_LIBRI + ".json");

    if (!response.ok) {
      throw new Error("Errore: " + response.status);
    }

    const dati = await response.json();
    const libri = listaOggetti(dati);

    initTable(libri);
    return libri;
  } catch (error) {
    console.log("Errore: " + error);
    initTable([]); // così la tabella si vede comunque
    return [];
  }
}

function initTable(libri) {
  // Se esiste già una DataTable, distruggila prima (evita doppia inizializzazione)
  if ($.fn.dataTable.isDataTable("#tableLibri")) {
    $("#tableLibri").DataTable().destroy();
  }

  // ricostruisci il tbody pulito (buona pratica con destroy/reinit)
  $("#tableLibri tbody").empty();

  const righe = libri.map((l) => {
    const btnElimina = `<button class="btn-elimina" data-id="${l.id}">Elimina</button>`;
    return [l.id, l.titolo, l.autore, l.categoria, btnElimina];
  });

  dt = $("#tableLibri").DataTable({
    data: righe,
    responsive: true,
    destroy: true,
    columnDefs: [
      { targets: 4, orderable: false, searchable: false }, // colonna Azione
    ],
  });
}

async function aggiungiLibro(libro) {
  try {
    const response = await fetch(URL_LIBRI + ".json", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(libro),
    });

    if (!response.ok) {
      throw new Error("Errore: " + response.status);
    }

    const dati = await response.json(); // Firebase => { name: "ID_GENERATO" }
    return { ...libro, id: dati.name };
  } catch (error) {
    console.error("Errore: " + error);
    return null;
  }
}

async function eliminaLibro(id) {
  try {
    const response = await fetch(`${URL_LIBRI}/${id}.json`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error("Errore: " + response.status);
    }

    return true;
  } catch (error) {
    console.error("Errore: " + error);
    return false;
  }
}

/* ---------- EVENTI ---------- */

const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const titoloEl = document.querySelector("#titolo");
  const autoreEl = document.querySelector("#autore");
  const categoriaEl = document.querySelector("#categoria");

  const titolo = titoloEl.value.trim();
  const autore = autoreEl.value.trim();
  const categoria = categoriaEl.value.trim();

  if (!titolo || !autore || !categoria) {
    alert("Inserire tutti i campi del libro");
    return;
  }

  const newLibro = new Libro({ titolo, autore, categoria });

  const dati = await aggiungiLibro(newLibro);

  if (dati) {
    document.getElementById("result").innerHTML =
      "Libro inserito correttamente con id " + dati.id;

    // refresh tabella subito (così lo vedi senza ricaricare pagina)
    await leggiLibri();
  } else {
    document.getElementById("result").innerHTML =
      "Errore durante l'inserimento del libro";
  }

  titoloEl.value = "";
  autoreEl.value = "";
  categoriaEl.value = "";
});

// Delegation: gestisce i click sui bottoni dentro DataTable
document.addEventListener("click", async (e) => {
  if (!e.target.classList.contains("btn-elimina")) return;

  const id = e.target.dataset.id;
  const ok = confirm("Vuoi eliminare il libro con id: " + id + " ?");
  if (!ok) return;

  const deleted = await eliminaLibro(id);

  if (deleted) {
    document.getElementById("result").innerHTML =
      "Libro eliminato correttamente (id " + id + ")";

    // refresh lista
    await leggiLibri();
  } else {
    document.getElementById("result").innerHTML =
      "Errore durante l'eliminazione del libro";
  }
});

/* ---------- AVVIO ---------- */
leggiLibri();