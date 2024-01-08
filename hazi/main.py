def fajlbol_olvas(fajl_nev):
    try:
        with open(fajl_nev, 'r') as fajl:
            return [[int(szam) for szam in sor.split()] for sor in fajl]
    except FileNotFoundError:
        print(f"A '{fajl_nev}' fájl nem található.")
        return None

def szamok_osszege(matrix):
    return sum(szam for sor in matrix for szam in sor)

def soronkenti_osszeg(matrix):
    return [sum(sor) for sor in matrix]

def oszloponkenti_osszeg(matrix):
    return [sum(oszlop) for oszlop in zip(*matrix)]

def menu_kiirasa():
    print("Menüpontok:")
    print("1. Számok összege")
    print("2. Számok soronkénti összege")
    print("3. Számok oszloponkénti összege")
    print("0. Kilépés")

def main():
    fajl_nev = "input.txt"
    matrix = fajlbol_olvas(fajl_nev)

    if matrix is None:
        return

    while True:
        menu_kiirasa()
        valasztas = input("Válassz egy menüpontot (0-3): ")

        if valasztas == "0":
            print("Kilépés...")
            break
        elif valasztas == "1":
            print(f"A számok összege: {szamok_osszege(matrix)}")
        elif valasztas == "2":
            for i, sor_osszeg in enumerate(soronkenti_osszeg(matrix), start=1):
                print(f"{i}. sor: {sor_osszeg}")
        elif valasztas == "3":
            for i, oszlop_osszeg in enumerate(oszloponkenti_osszeg(matrix), start=1):
                print(f"{i}. oszlop: {oszlop_osszeg}")
        else:
            print("Érvénytelen választás. Kérlek, válassz újra.")

if __name__ == "__main__":
    main()
