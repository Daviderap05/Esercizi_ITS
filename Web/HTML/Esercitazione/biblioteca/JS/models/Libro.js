// models/Libro.js
export class Libro {
  constructor({ id = null, titolo, autore, categoria, disponibile = true }) {
    this.id = id;
    this.titolo = titolo;
    this.autore = autore;
    this.categoria = categoria;
    this.disponibile = disponibile;
  }
}
