package Esercitazioni.StudioMedico;

import java.time.LocalDate;

public class Appuntamento {

    public Medico medico;
    public Paziente paziente;
    public LocalDate data;
    public String ora;

    public Appuntamento(LocalDate data, Medico medico, String ora, Paziente paziente) {
        this.data = data;
        this.medico = medico;
        this.ora = ora;
        this.paziente = paziente;
    }

    
}
