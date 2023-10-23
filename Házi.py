'''def szigoruan_monoton_novekvo(szamok):
    n = len(szamok)
    for i in range(1, n):
        if szamok[i] <= szamok[i - 1]:
            return False
    return True

szamlista = [1, 10, 784, 63, 309]
if szigoruan_monoton_novekvo(szamlista):
    print("A számlista szigorúan monoton növekvő")
else:
    print("A számlista nem szigorúan monoton növekvő")'''



def atvaltas_tizes_szamrendszerbe(szam, forras_szamrendszer):
    tizes_szamrendszerben = 0
    for i, jegy in enumerate(reversed(szam)):
        tizes_szamrendszerben += int(jegy) * (forras_szamrendszer ** i)
    return tizes_szamrendszerben

def atvaltas_mas_szamrendszerbe(tizes_szamrendszerben, cel_szamrendszer):
    eredmeny = ''
    while tizes_szamrendszerben > 0:
        maradek = tizes_szamrendszerben % cel_szamrendszer
        eredmeny = str(maradek) + eredmeny
        tizes_szamrendszerben //= cel_szamrendszer
    return eredmeny

def main():
    forras_szamrendszer = int(input("Kérem a forrás számrendszer alapszámát (pl. 2, 8, 10 stb.): "))
    cel_szamrendszer = int(input("Kérem a cél számrendszer alapszámát (pl. 2, 8, 10 stb.): "))
    szam = input("Kérem a konvertálni kívánt számot: ")

    tizes_szamrendszerben = atvaltas_tizes_szamrendszerbe(szam, forras_szamrendszer)
    eredmeny = atvaltas_mas_szamrendszerbe(tizes_szamrendszerben, cel_szamrendszer)

    print(f"A(z) {szam} szám {forras_szamrendszer} számrendszerből átkonvertálva {cel_szamrendszer} számrendszerbe: {eredmeny}")

if __name__ == "__main__":
    main()
