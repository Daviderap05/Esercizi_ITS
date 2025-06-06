from Progettazione.VoliAerei import aereoporto, compagnia
from Progettazione.VoliAerei.tipi_di_dato.codiceVolo import CodiceVolo
from Progettazione.VoliAerei.tipi_di_dato.durataVolo import DurataVolo


class Volo:
    
    def __init__(self, codice: CodiceVolo, durata: DurataVolo, arrivo: aereoporto.Aereoporto, partenza: aereoporto.Aereoporto, volo_comp: compagnia.CompagniaAerea) -> None:
        
        
        if not codice or not isinstance(codice, CodiceVolo):
            
            raise ValueError("Codice volo non valido")
        
        if not durata or not isinstance(durata, DurataVolo):
            
            raise ValueError("Durata volo non valida")
        
        if not arrivo or not isinstance(arrivo, aereoporto.Aereoporto):
            
            raise ValueError("Aereoporto di arrivo non valido")
        
        if not partenza or not isinstance(partenza, aereoporto.Aereoporto):
            
            raise ValueError("Aereoporto di partenza non valido")
        
        if not volo_comp or not isinstance(volo_comp, compagnia.CompagniaAerea):
            
            raise ValueError("Compagnia aerea non valida")
        
        self.codice = codice
        self.durata = durata
        self.setArrivo(arrivo)
        self.setPartenza(partenza)
        self.setCompagnia(volo_comp)
        
    def __str__(self) -> str:
        
        return f"Codice volo: {self.codice}, durata volo - {self.durata}, arrivo - {self._arrivo}, partenza - {self._partenza}"
    
    def getCodice(self) -> CodiceVolo:
        
        return self.codice
    
    def getDurata(self) -> DurataVolo:
        
        return self.durata
    
    def setCodice(self, codice: CodiceVolo) -> None:
        
        if not codice or not isinstance(codice, CodiceVolo):
            
            raise ValueError("Codice non valido")
        
        self.codice = codice
        
    def setDurata(self, durata: DurataVolo) -> None:
        
        if not durata or not isinstance(durata, DurataVolo):
            
            raise ValueError("Durata non valida")
        
        self.durata = durata
        
        
    def setArrivo(self, arrivo: aereoporto.Aereoporto) -> None:
        
        if not arrivo or not isinstance(arrivo, aereoporto.Aereoporto):
            
            raise ValueError("Aereoporto di arrivo non valido")
        
        self._arrivo = arrivo
        
    def setPartenza(self, partenza: aereoporto.Aereoporto) -> None:
        
        if not partenza or not isinstance(partenza, aereoporto.Aereoporto):
            
            raise ValueError("Aereoporto di partenza non valido")
        
        self._partenza = partenza
        
    def setCompagnia(self, volo_comp: compagnia.CompagniaAerea) -> None:
        
        if not volo_comp or not isinstance(volo_comp, compagnia.CompagniaAerea):
            
            raise ValueError("Compagnia aerea non valida")
        
        self._volo_comp = volo_comp
        
    def getArrivo(self) -> aereoporto.Aereoporto:
        
        return self._arrivo
    
    def getPartenza(self) -> aereoporto.Aereoporto:
        
        return self._partenza
    
    def getCompagnia(self) -> compagnia.CompagniaAerea:
        
        return self._volo_comp