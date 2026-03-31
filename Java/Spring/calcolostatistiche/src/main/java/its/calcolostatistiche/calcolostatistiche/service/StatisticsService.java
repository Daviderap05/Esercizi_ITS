package its.calcolostatistiche.calcolostatistiche.service;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

import org.springframework.stereotype.Service;

@Service
public class StatisticsService {

    private final Map<String, Integer> usageStats = new ConcurrentHashMap<>();

    public void incrementaUso(String methodName) {
        usageStats.put(methodName, usageStats.getOrDefault(methodName, 0) + 1);
    }

    // Servizio per mostrare la frequenza d'uso di una singola funzionalità
    public int getFrequenzaOperazione(String operation) {
        return usageStats.getOrDefault(operation, 0);
    }

    // Servizio che torna il report complessivo con tutte le occorrenze
    public Map<String, Integer> getReportComplessivo() {
        return usageStats;
    }
}
