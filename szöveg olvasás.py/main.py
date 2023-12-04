fajlnev="input.txt"
f=open(fajlnev, "r")
sorok=f.readlines()
f.close()
for i in range(len(sorok)):
    sorok[i]=sorok[i].strip()
print(sorok[0])
sum=int(sorok[1])+int(sorok[2])
print(sum)





