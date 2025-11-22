from datetime import date


class Bid:

    istante: date # immutabile, noto alla nascita    

    def __init__(self, istante: date) -> None:
        self._istante = istante

    def getIstante(self) -> date:
        return self._istante