import sys
filename=sys.argv[1]
print(filename)

file=open(filename)
sorok=file.readlines()
file.close()

for i in range(len(sorok)):
    print(sorok[i].strip())