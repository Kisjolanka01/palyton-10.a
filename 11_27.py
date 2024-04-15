#Feladat: feltétel szerimti adatbekérés

intervallum_min=3
intervallum_max=15

x = input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]")
x = int(x)
if x>intervallum_min and x<intervallum_max:
    print("jo számot adtal meg")
else:
    print("nem jo szamot adtal meg")

feltetel=False
while not feltetel:
    x = input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]")
    x=int(x)
    if x>=intervallum_min and x<=intervallum_max:
        feltetel=True
    else:
        print("jo szamot adtal meg")


hetnapjai=["Hétfő", "Kedd"]
hetek=[]
for hetszama in range(x):
    lista=[]
    for nap in hetnapjai:
        ert=input(input(f"Add meg hogy  hány támadás érte az állatkertet({hetszama+1}.hét {nap})"))
    lista.append(ert)
    print(lista)
    hetek.append(lista)
print(hetek)

hetek_str=[]
for i in range(len(hetek)):
    lista=[]
    for j in range(len(hetek[i])):
        lista.append(str(hetek[i][j]))
    hetek_str.append(lista)
        
for het_szamlalo in range(len(hetek)):
    tamadasok=" ".join(hetek_str[het_szamlalo])
    print(f"{het_szamlalo}.het: {tamadasok}")

for het_szamlalo in range(len(hetek)):
    str_=str(het_szamlalo)+". hét:"
    for nap_szamlalo in range(len(hetek[het_szamlalo])):
        str_+=str([het_szamlalo] [nap_szamlalo])+" "
print(str_)