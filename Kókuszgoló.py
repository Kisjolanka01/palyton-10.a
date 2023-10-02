import random
eladasok = 0
sin = 1


def feltoltes_adatszerkezet():
    for i in range(10):
        eladasok[i] = 1

def osszes_eladas():
    return sum(eladasok)


def heti_eladas(het):
    return eladasok[het]

def legsikeresebb_het():
    return eladasok.index(max(eladasok))

def eladasmentes_napok():
    return eladasok.count(0)

def legkevesebb_paratlan_eladas_nap():
    min_paratlan = min(eladasok[1::2])
    return eladasok.index(min_paratlan)

print("osszes eladas",osszes_eladas())
print("heti eladas(4.heti):", heti_eladas(4))
print("legsikeresebb het", legsikeresebb_het())
print("eladas mentes napok:", eladasmentes_napok())
print(" legkevesebb paratlan eladas nap", legkevesebb_paratlan_eladas_nap())
