from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, ar):
        self.rendszam = rendszam
        self.tipus = tipus
        self.ar = ar
        self.elheto = True

    @abstractmethod
    def __str__(self):
        pass

class Szemelyauto(Auto):
    def __str__(self):
        return f"Személyautó - {self.rendszam}, {self.tipus}, {self.ar} Ft/nap"

class Teherauto(Auto):
    def __str__(self):
        return f"Teherautó - {self.rendszam}, {self.tipus}, {self.ar} Ft/nap"