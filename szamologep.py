print("1. összeadás")
print("2. összeszorzás")
print("3. átlag")

while True:
    valaszstr=input("adj me egyszámot!")
    if valaszstr.isdecimal():
        valasz=int(valaszstr)
        break

def add(x,y):
    sum=x+y
    return sum
def szoroz(x,y):
    sum = x*y
    return sum
def atlag(x,y):
    sum = add(x,y)
    return sum/2

def megad():
    szam1=int(input("Elso szam"))
    szam2=int(input("masodik szam"))
    return (szam1,szam2)

if valasz == 1:
    szam1,szam2=megad()
    print(megad(szam1,szam2))
elif valasz == 2:
    szam1,szam2=megad()
    print(szoroz(szam1,szam2))

elif valasz == 3:
    szam1,szam2=megad()
    print(atlag(szam1,szam2))


