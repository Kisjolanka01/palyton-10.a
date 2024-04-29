import random
while True:
    szam = int(input("Add meg a lista méretét[5...25]:"))
    if 5<= szam <=25:
        break
    print("Hibás adatbeitel! Próbálja újra!")
    számok=[]
    osszeg=0
    db=0
    negativelemek=0
    for i in range(szam):
        számok.append(random.randint(-10,10))
        osszeg=+számok[i]
        if számok[i]==0:
            db+=1
        if számok[i]<0:
            negativelemek+=1
        print(f'A lista tartalma:{számok}')
        print(f'A listában lévő elemek összege:{osszeg}')
        print(f'A listaban lévő 0 elemek száma:{db}')
        print(f'A listaban lévő negativ elemek száma:{negativelemek}')
        