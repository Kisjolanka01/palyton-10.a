s = input("adj meg egy szamot")
if int(s)%2==0:
    print('a szam oszthato 2-vel')

string =  input("adj meg egy szamot")
if "a" in string:
    print("az a betű benne van a szoban")

for i in range(len(string)):
    if string[i] == "a":
        hely = i+1
print(hely)