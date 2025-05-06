class Berles:
    def __init__(self, auto, berlo_nev, datum):
        self.auto = auto
        self.berlo_nev = berlo_nev
        self.datum = datum

    def __str__(self):
        return f"{self.berlo_nev} - {self.auto.rendszam} ({self.auto.tipus}) - {self.datum}"