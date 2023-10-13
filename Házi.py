def szigoruan_monoton_novekvo(szamok):
    n = len(szamok)
    for i in range(1, n):
        if szamok[i] <= szamok[i - 1]:
            return False
    return True

szamlista = [1, 10, 784, 63, 309]
if szigoruan_monoton_novekvo(szamlista):
    print("A számlista szigorúan monoton növekvő")
else:
    print("A számlista nem szigorúan monoton növekvő")
