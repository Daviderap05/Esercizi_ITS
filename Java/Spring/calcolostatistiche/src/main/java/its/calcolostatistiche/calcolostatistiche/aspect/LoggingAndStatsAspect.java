package its.calcolostatistiche.calcolostatistiche.aspect;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import its.calcolostatistiche.calcolostatistiche.service.StatisticsService;

@Aspect
@Component
public class LoggingAndStatsAspect {

    private static final Logger logger = LoggerFactory.getLogger(LoggingAndStatsAspect.class);
    private final StatisticsService statisticsService;

    public LoggingAndStatsAspect(StatisticsService statisticsService) {
        this.statisticsService = statisticsService;
    }

    @Around("execution(* com.example.demo.service.CalculatorService.*(..))")
    public Object tracciaEStatistiche(ProceedingJoinPoint joinPoint) throws Throwable {
        String methodName = joinPoint.getSignature().getName();

        // Aggiorniamo le statistiche prima dell'esecuzione
        statisticsService.incrementaUso(methodName);

        try {
            // Procede con l'esecuzione del metodo originale
            Object result = joinPoint.proceed();

            // Log in caso di successo
            logger.info("Metodo eseguito con SUCCESSO: {}", methodName);
            return result;

        } catch (Throwable ex) {
            // Log in caso di eccezione
            logger.error("Metodo terminato con ECCEZIONE: {} - Motivo: {}", methodName, ex.getMessage());
            throw ex; // Rilanciamo l'eccezione per farla gestire al controller
        }
    }
}
