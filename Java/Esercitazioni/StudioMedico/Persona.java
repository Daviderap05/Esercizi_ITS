package Esercitazioni.StudioMedico;

public abstract class Persona {
    private String nome;

    public Persona(String nome) {
        setNome(nome);
    }

    public String getNome() {
        return this.nome;
    }

    // final = i figli non possono fare l'override
    public final void setNome(String nome) throws IllegalArgumentException {
        if (nome == null || nome.isBlank()) {
            throw new IllegalArgumentException("Il nome non può essere vuoto o nullo");
        }

        this.nome = nome;
    }
}
