# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!
filename="input.txt"
file=open(filename,"r")
file_lista=file.readlines()
file.close()

print(file_lista)
name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    name_list.append(lista_parts[0])

    lista_parts=file_lista[i].strip().split()

    _l=[]
    for j in range(1,len(lista_parts)):
        _l.append(int(lista_parts[j]))
    pancake_list.append(_l)

print(name_list)
print(pancake_list)
for i in range(len(pancake_list)):
    print(len(pancake_list[i]))

#print(file_lista)
# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
fejlec="Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
print(fejlec)