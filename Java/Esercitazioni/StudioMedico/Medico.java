package Esercitazioni.StudioMedico;

public class Medico extends Persona {

    private String specializzazione;

    public Medico(String nome, String specializzazione) {
        super(nome);
        setSpecializzazione(specializzazione);
    }

    public String getSpecializzazione() {
        return this.specializzazione;
    }

    public final void setSpecializzazione(String specializzazione) {
        if (specializzazione == null || specializzazione.isBlank()) {
            throw new IllegalArgumentException("La specializzazione non può essere vuota o nulla");
        }

        this.specializzazione = specializzazione;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Medico{");
        sb.append("nome='").append(getNome()).append("'");
        sb.append(", specializzazione='").append(this.specializzazione).append("'");
        sb.append('}');
        return sb.toString();
    }
}
