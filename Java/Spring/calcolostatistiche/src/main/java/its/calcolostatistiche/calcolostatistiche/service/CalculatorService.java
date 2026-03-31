
package its.calcolostatistiche.calcolostatistiche.service;

import org.springframework.stereotype.Service;

@Service
public class CalculatorService {

    public double somma(double a, double b) {
        return a + b;
    }

    public double sottrazione(double a, double b) {
        return a - b;
    }

    public double moltiplicazione(double a, double b) {
        return a * b;
    }

    public double divisione(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("Impossibile dividere per zero"); //
        }
        return a / b;
    }
}