'''s = input("adj meg egy szamot: ")
if int(s)%2==0:
    print('a szam oszthato 2-vel')
    print("------")

str =  input("adj meg egy szot: ")
if "a" in str:
    print("az a betű benne van a szoban")
    print("------")


for i in range(len(string)):
    if str[i] == "a":
        hely = i
print(hely+1)
print("------")
'''
'''
mondatok = 0
str="Első mondat. Második mondat!"
for i in range(len(str)):
    if (str[i] =='.'
    or str[i]== '!'
    or str[i]== '?'):
        mondatok =mondatok+1
print(f"{mondatok} mondat van")
'''


Lista=[
    ["Béla","F","18.00"],
    ["Judit","N","18.01"],
    ["Zoli","F","18:05"],
]
egysor = ""
for i in range(len(Lista)):
    #print(Lista[i])
    for j in range(len(Lista[i])):
        egysor+=Lista[i][j]
print(egysor)



i=0
while(not(Lista[i][1]=="N")):
    i=i+1
    print(Lista[i][0])