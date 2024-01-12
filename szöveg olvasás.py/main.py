# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input.txt"

file=open(filename, "r")
file_lista=file.readlines()
file.close()

name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    _lista=file_lista[i].strip()
    _lista_parts=_lista.split()

    # így is lehet: _lista_parts=file_lista[i].strip().split()
    name_list.append(_lista_parts[0])

    _l=[]
    for j in range(1,len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    pancake_list.append(_l)

# print(name_list)
# print(pancake_list)
# for i in range(len(pancake_list)):
#     print(len(pancake_list[i]))

# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
fejlec="Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
print(fejlec)
for i in range(len(name_list)):
    print(name_list[i], "\t")
for x in range(len(pancake_list[i])):
    print(pancake_list[i][x], end="\t")
    if x == 11:
        print("\n")

# 3) Add meg, hogy márciusban ki sütötte a legtöbb palacsintát!
marc=pancake_list[0][2]
marc= name_list[0]
for i in range (len(name_list)):
    if pancake_list[i] [2] >= marc:
        marc = pancake_list[i][2]
        marcind =name_list[i]
print("Márciusban {marcing} sütöttek a legetöbb palacsintat")
# 4) Add meg, hogy ki sütötte az évben a legkevesebb palacsintát!
legkevesebb = pancake_list[0]
for i in range(len(pancake_list)):
    if sum(pancake_list[i]) <= legkevesebb:
        legkevesebb = sum(pancake_list[i])
        legind= name_list[i]
print(f"Az évben {legind} sütött a legkevesebb palacsintát")
# 5) Add meg, hogy az a személy, akinek B-vel kezdődik a neve, Májusban hány palacsintát sütött.
for i in range(len(name_list)):
    if name_list[i] [0] =="B":
        print(f" Májusban {pancake_list[i][4]} palacsintat sutott az az ember,akinek B-vel kezodik a neve")
# 6) Volt-e olyan személy, akinek az évben változó teljesítménye volt?
#       Pl: sütött valamennyit, majd a következő hónapban többet, a következőben az előzőnél kevesebbet stb
#       írd ki a személy nevét!
valtozo= []
for i in range(len(pancake_list)):
    for x in range(len(pancake_list)[i]):
        if pancake_list[i][x]> pancake_list[i][x+1] and pancake_list[i][x+1]:
            valtozo.append(".")
            