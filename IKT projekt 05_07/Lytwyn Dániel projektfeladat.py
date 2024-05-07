while True:
    listameret = int(input('Add meg a lista méretét [10...20]: '))
    if listameret >= 10 and listameret <= 20:
        break
    print('Hibás adatbevitel! Próbáld újra!')

import random
elemek = []
i = 0
while i < listameret:
    elemek.append(random.randint(1, 5))
    i += 1
print(f'A lista tartalma: {elemek}')

elemosszeg = 0
i = 0
while i < len(elemek):
    elemosszeg = elemosszeg + elemek[i]
    i += 1
print(f'A listában lévő elemek összege: {elemosszeg}')

legnagyobb = elemek[0]
legnagyobbhely = 0
i = 0
while i < len(elemek):
    if elemek[i] > legnagyobb:
        legnagyobb = elemek[i]
        legnagyobbhely = i
    i += 1
print(f'A listában lévő legnagyobb elem: {legnagyobb}, helye: {legnagyobbhely + 1}. pozíció')

def adatokBeolvasása(fajl):
    lista = []
    f = open(fajl, 'r', encoding='UTF-8')
    s = f.readlines()
    i = 0
    while i < len(s):
        lista.append(s[i].strip().split())
        i += 1
    f.close()
    i = 0
    while i < len(lista):
        j = 1
        while j < len(lista[i]):
            lista[i][j] = int(lista[i][j])
            j += 1
        i += 1
    return lista

def nullaKm(lista):
    db = 0
    i = 0
    while i < len(lista):
        j = 1
        while j < len(lista[i]):
            if lista[i][j] == 0:
                db += 1
            j += 1
        i += 1
    return db
lista = adatokBeolvasása('fuvarok.txt')
dbKm = nullaKm(lista)
print(f'Az adatbázisban {dbKm} db 0 km havi futásteljesítményt tartalmazó hónap van.')