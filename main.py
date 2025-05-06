from kolcsonzo import Autokolcsonzo

def menu():
    print("\n--- AUTÓKÖLCSÖNZŐ ---")
    print("1 - Autó bérlése")
    print("2 - Bérlés lemondása")
    print("3 - Aktuális bérlések")
    print("0 - Kilépés")

def main():
    kolcsonzo = Autokolcsonzo("CityRent")
    kolcsonzo.betolt_alapadatok()

    while True:
        menu()
        valaszt = input("Választás: ")

        if valaszt == "1":
            rendszam = input("Rendszám: ")
            nev = input("Bérlő neve: ")
            datum = input("Bérlés dátuma (ÉÉÉÉ-HH-NN): ")
            kolcsonzo.berel(rendszam, nev, datum)

        elif valaszt == "2":
            rendszam = input("Rendszám: ")
            nev = input("Bérlő neve: ")
            kolcsonzo.lemondas(rendszam, nev)

        elif valaszt == "3":
            kolcsonzo.listaz_berlesek()

        elif valaszt == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()