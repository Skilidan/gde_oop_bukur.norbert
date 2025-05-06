from auto import Szemelyauto, Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaad(self, auto):
        self.autok.append(auto)

    def berel(self, rendszam, berlo_nev, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam and auto.elheto:
                auto.elheto = False
                uj_berles = Berles(auto, berlo_nev, datum)
                self.berlesek.append(uj_berles)
                print("Sikeres bérlés! Ár:", auto.ar, "Ft")
                return
        print("Nem elérhető vagy nem létező autó.")

    def lemondas(self, rendszam, berlo_nev):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.berlo_nev == berlo_nev:
                berles.auto.elheto = True
                self.berlesek.remove(berles)
                print("Bérlés sikeresen lemondva.")
                return
        print("Nincs ilyen bérlés.")

    def listaz_berlesek(self):
        if not self.berlesek:
            print("Nincs aktív bérlés.")
        for b in self.berlesek:
            print(b)

    def betolt_alapadatok(self):
        self.auto_hozzaad(Szemelyauto("ABC123", "Toyota Corolla", 10000))
        self.auto_hozzaad(Szemelyauto("XYZ789", "Ford Focus", 12000))
        self.auto_hozzaad(Teherauto("TRK001", "MAN TGL", 20000))

        self.berel("ABC123", "Kovács Béla", "2025-04-01")
        self.berel("XYZ789", "Nagy Anna", "2025-04-02")
        self.berel("TRK001", "Tóth Sára", "2025-04-03")
        self.berel("ABC123", "Péter Ákos", "2025-04-04")