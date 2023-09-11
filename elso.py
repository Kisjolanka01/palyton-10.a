nemjo = True
while nemjo:
    szam_str= input('szám:')
    if szam_str.isdecimal():
        nemjo=False
        szam=int(szam_str)
if szam >3:
    print("nagyobb")
elif szam <3:
    print("kisebb")