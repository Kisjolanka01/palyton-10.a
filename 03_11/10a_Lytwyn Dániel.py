"""
1. Fájl átnevezése: osztály_név.py

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet!
3. feladat1(): számold ki a fájlban található számok összegét a tanult prog tétel segítségével!
4. feladat2(): számold ki a fájlban található számok átlagát a tanult prog tétel segítségével!
5. feladat3(): számold ki a fájlban található számok minimumát a tanult prog tétel segítségével!
6. feladat4(): számold ki a fájlban található számok maximumát a tanult prog tétel segítségével!

Kiírások:
feladat1: [eredmény]
feladat2: [eredmény]
feladat3: [eredmény]
feladat4: [eredmény]
A ": " után csak az eremény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas2] név 
"""
def beolvas(filename):
    file = open(filename, encoding='utf-8')
    sor = file.read()
    file.close()
    adat = sor.split(",")
    lista = []
    for i in range(1,len(adat)-1):
        lista.append(int(adat[i]))
    return(lista)


def feladat1(filename):
    lista = beolvas(filename)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return(osszeg)


def feladat2(filename):
    lista = beolvas(filename)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    atlag =  osszeg/len(lista)
    return(atlag)


def feladat3(filename):
    lista = beolvas(filename)
    minimum = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimum:
            minimum = lista[i]
    return(minimum)
    
def feladat4():
    pass
    

print(f"1. Feladat:{feladat1("input")}")
print(f"2. Feladat:{feladat2("input")}")
print(f"3. Feladat:{feladat3("input")}")
print()
