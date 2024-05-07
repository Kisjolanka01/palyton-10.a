import random
while True:
    szam = int(input("Add meg a lista méretét[10...20]:"))
    if 10<= szam <=20:
        break
    print("Hibás adatbeitel! Próbálja újra!")
    elemek=[]
    osszeg=0
    for i in range(szam):
        elemek.append(random.randint(1,5))
        osszeg=+elemek[i]
        print(f'A listában lévő elemek összege{osszeg}')
        print(f'A lista tartalma{elemek}')
        maxert=0
        index=0
        for i in range(1,len(elemek)):
            if elemek[i]> maxert:
                maxert = elemek[i]
                index=i+1
                print(f'a legnagyobb elem: {maxert}, helye: {index},pozicio')
