package its.calcolostatistiche.calcolostatistiche.controller;

import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import its.calcolostatistiche.calcolostatistiche.service.CalculatorService;
import its.calcolostatistiche.calcolostatistiche.service.StatisticsService;

@RestController
@RequestMapping("/api")
public class CalculatorController {

    private final CalculatorService calculatorService;
    private final StatisticsService statisticsService;

    public CalculatorController(CalculatorService calculatorService, StatisticsService statisticsService) {
        this.calculatorService = calculatorService;
        this.statisticsService = statisticsService;
    }

    @GetMapping("/somma")
    public double somma(@RequestParam double a, @RequestParam double b) {
        return calculatorService.somma(a, b);
    }

    @GetMapping("/divisione")
    public double divisione(@RequestParam double a, @RequestParam double b) {
        return calculatorService.divisione(a, b);
    }

    @GetMapping("/statistiche/{operazione}")
    public int singolaStatistica(@PathVariable String operazione) {
        return statisticsService.getFrequenzaOperazione(operazione);
    }

    @GetMapping("/statistiche/report")
    public Map<String, Integer> reportCompleto() {
        return statisticsService.getReportComplessivo();
    }
}
