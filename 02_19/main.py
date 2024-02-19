filename="02_19/file.txt"

file=open(filename, "r")
file_lista=file.readlines()
file.close()
nevek = ["gomboc", "fagyi", "golyo"]
lista=[]
for i in range(len(file_lista)):
    _lista_parts=file_lista[i].strip().split()
    _l=[]
    for j in range(1,len(_lista_parts)):
        _l.append(_lista_parts[j])
    lista.append(_l)
del lista[1]
for i in range(len(lista)):
    for x in range(len(lista[i])):
        lista[i][x] = int(lista[i][x])
osszes = 0
for i in range(len(lista)):
    for x in range(len(lista[i])):
        osszes += lista[i][x]
    print(f"Osszes eladott {nevek[i]}: {osszes}")
