import random

 # 1.Feladat

def lista_letrehozas():
    elemszam = int(input("Adja meg a lista elemszámát: "))
    szamok = [random.randint(-100, 100) for _ in range(elemszam)]
    return szamok
szamok = lista_letrehozas()
print(szamok)

# 2.Feladat

def intervallum_kiiras(szamok):
    kezdo = int(input("Adja meg a kezdő sorszámot: "))
    vege = int(input("Adja meg a befejező sorszámot: "))

    while vege >= len(szamok) or vege < kezdo:
        print("Érvénytelen befejező sorszám. Adjon meg újra érvényes értéket.")
        vege = int(input("Adja meg a befejező sorszámot: "))
    print(szamok[kezdo:vege+1])
intervallum_kiiras(szamok)

# 3.Feladat

def osszeg_es_szorzat(szamok, kezdo, vege):
    intervallum_osszeg = sum(szamok[kezdo:vege+1])
    szorzat = szamok[kezdo] * szamok[vege]

    if intervallum_osszeg > szorzat:
        print("Az intervallum számjegyeinek összege nagyobb.")
    elif intervallum_osszeg < szorzat:
        print("Az intervallum első és utolsó számának szorzata nagyobb.")
    else:
        print("Az intervallum számjegyeinek összege egyenlő a szorzatával.")
osszeg_es_szorzat(szamok, 2, 5)

# 4.Feladat

def min_max_tartalmazas(szamok, kezdo, vege):
    min_szam = szamok[kezdo]
    max_szam = szamok[vege]

    for szam in szamok:
        if szam < min_szam:
            min_szam = szam
        if szam > max_szam:
            max_szam = szam

    if min_szam in szamok and max_szam in szamok:
        print("A legkisebb és legnagyobb szám előfordul a listában.")
    else:
        print("A legkisebb vagy legnagyobb szám nem fordul elő a listában.")
min_max_tartalmazas(szamok, 2, 5)

# 5.Feladat

def min_elofordulas_szamolas(szamok, kezdo, vege):
    min_szam = min(szamok[kezdo:vege+1])
    elofordulas_szam = szamok.count(min_szam)
    print(f"A legkisebb elem ({min_szam}) a listában {elofordulas_szam} alkalommal szerepel.")
min_elofordulas_szamolas(szamok, 2, 5)

# 6.Feladat

def legnagyobb_negativ_szam(szamok):
    legnagyobb_negativ = None
    index = None

    for i, szam in enumerate(szamok):
        if szam < 0 and (legnagyobb_negativ is None or szam > legnagyobb_negativ):
            legnagyobb_negativ = szam
            index = i

    if index is not None:
        print(f"A legnagyobb negatív szám ({legnagyobb_negativ}) a(z) {index+1}. helyen található.")
    else:
        print("A listában nincs negatív szám.")

legnagyobb_negativ_szam(szamok)
