def beolvas_input_fajl(fajlnev):
    try:
        with open(fajlnev, 'r') as fajl:
            sorok = fajl.readlines()
            return [list(map(int, sor.strip().split())) for sor in sorok]
    except FileNotFoundError:
        print(f"A(z) {fajlnev} fájl nem található.")
        return None

def sorok_osszege(matrix):
    return [sum(sor) for sor in matrix]

def oszlopok_osszege(matrix):
    oszlopok_szama = len(matrix[0])
    return [sum(matrix[sor][oszlop] for sor in range(len(matrix))) for oszlop in range(oszlopok_szama)]

def menu_megjelenitese():
    print("\nMenüpontok:")
    print("1. Számok összege")
    print("2. Számok soronkénti összege")
    print("3. Számok oszloponkénti összege")
    print("0. Kilépés")

szamok = beolvas_input_fajl("input.txt")
if szamok is None:
    exit(1)

while True:
    menu_megjelenitese()
    valasztas = input("Válassz egy menüpontot (0-3): ")

    if valasztas == '0':
        print("Viszontlátásra!")
        break
    elif valasztas == '1':
        print(f"A számok összege: {sum(sum(sor) for sor in szamok)}")
    elif valasztas == '2':
        sor_osszegek = sorok_osszege(szamok)
        for i, sor_osszeg in enumerate(sor_osszegek, start=1):
            print(f"{i}. sor: {sor_osszeg}")
    elif valasztas == '3':
        oszlop_osszegek = oszlopok_osszege(szamok)
        for i, oszlop_osszeg in enumerate(oszlop_osszegek, start=1):
            print(f"{i}. oszlop: {oszlop_osszeg}")
    else:
        print("Érvénytelen választás. Kérlek, válassz újra.")
