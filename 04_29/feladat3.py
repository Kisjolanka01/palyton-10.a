def adatbeolvasas(filename):
    file=open(filename,encoding="utf-8")
    sorok=file.readlines()
    file.close()
    lista=[]
    for i in range(len(sorok)):
        sorok[i]=sorok[i].strip
        lista.append(sorok[i].split())
    for i in range(len(lista[i])):
        for x in range(len(lista[i])):
            if x >0:
                lista[i][x] = int(lista[i][x])
    return lista
def nullakilometer(lista):
        szam = 0
        for i in range(len(lista)):
            for x in range(1,len(lista[i])):
                 if lista[i][x] ==0:
                    szam +=1
        return szam

print(f'AZ adatbázisban {nullakilometer}db 0km havi futásteljesítményt tartalmazó hónap van')

                
