export function listaOggetti(dati) {
  if (!dati) return []; // quando Firebase ritorna null (nessun dato)
  return Object.keys(dati).map((id) => ({ id, ...dati[id] }));
}
