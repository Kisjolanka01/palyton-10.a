import file_fvk as file

sorok=file.beolvas("input")
szamok=file.strListtoIntList(sorok,1,1)
print(szamok)


print(f"1.feladat: {len(szamok)}db szám van")

s=0
for i in range(len(szamok)):
    s+=szamok[i]
print(f"2.feladat: szamok osszege{s}")


s=1
for i in range(len(szamok)):
    s*szamok[i]
print(f"3.feladat: szamok szorzata{s}")

max=szamok[0]
for i in range(1, len(szamok)):
    if max<szamok[i]:
        max=szamok[i]
print(f"4.feladat: legnagyobb szam {max}")


print(f"5.feladat: 3. szam erteke {szamok[2]}")


min = 10000000
for i in range(len(szamok)):
    if szamok[i]%2==1 and szamok[i]<min:
        min=szamok[i]

