package Esercitazioni.StudioMedico;

public class Paziente extends Persona {

    private String email;

    public Paziente(String nome, String email) {
        super(nome);
        setEmail(email);
    }

    public String getEmail() {
        return this.email;
    }

    public final void setEmail(String email) throws IllegalArgumentException {
        String regex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";

        if (email == null || !email.matches(regex)) {
            throw new IllegalArgumentException("Formato email non valido");
        }
        this.email = email;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Paziente{");
        sb.append("nome='").append(getNome()).append("'");
        sb.append(", email='").append(this.email).append("'");
        sb.append('}');
        return sb.toString();
    }
}