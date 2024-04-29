def adatbeolvasas(filename):
    file=open(filename,encoding="utf-8")
    sorok=file.readlines()
    file.close()
    lista=[]
    for i in range(len(sorok)):
        sorok[i]=sorok[i].strip
        print(sorok)
        lista.append(sorok[i].split())
