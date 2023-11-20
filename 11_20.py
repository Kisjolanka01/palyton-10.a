'''
def fejlec(cim):
    szelesseg = 30
    csillagok = '*'*szelesseg
    kozepso_csillag = "*"*int(((szelesseg-len(cim))/2)-1)
    print(csillagok)
    if len(cim)%2==1:
        print(kozepso_csillag+' '+cim+' '+kozepso_csillag+'*')
    else:
        print(kozepso_csillag+' '+cim+' '+kozepso_csillag)
    print(csillagok)

program_neve ='Programcime'
fejlec(program_neve)

teszt=''
for i in range(2,20):
    teszt+='c'
    fejlec(teszt)

print(11_123_321)
print(0o123)#8as számrendszer
print(0xABBA)#16os számrendszer
print(0b11000000)#2es szamrendszer
x = int("345",8)#
print(x)

x=oct(321)
print(x)

x = hex(6000)
print(x)

x=bin(192)
print(x)


print(1/100000000)


str= 'Anya azt mondta hogy: "erj haza idoben!"'
print(str)

str= 'Anya azt mondta hogy: \"erj haza idoben!\"'
print(str)

x= 6/4
y=6//4
y=6//-4
z=6%4
print(x)
print(y)
print(z)
z= 6%4
zs = 2**5
print(9 % 6 % 2)

#x = input("X=")
#input("y=")



x="ha"*3
print(x)

x= 3 ==2
print(x)
x=3 !=2
print(x)

x=3
if x==3:
    print("az x értéke 3")
elif x<3:
    print("Az x értéke nem 3")
else:
    print("egyik feltétel sem igaz")
x=5
feltetel=True
while feltetel:
    print("ciklusmag")
    if(x==7):
        feltetel=False
    x+=1
print(x)



i=1
while True:
    print("Szeretem a puskast")
    i+=1'''


'''
while not True:
    pass


for i in range(10):
    pass #0 - 9
for i in range(2,5):
    pass
for i in range(2,10,3):
    pass
#brake
#continue

x = "szia"
for i in x:
    print(i)

x=5
while x<4:
    pass
else:
    print("nem lépett bele a ciklusba")

ijk=7
for ijk in range(10):
    print(ijk)
else:
    print("else ág:",ijk)


x=3
y=6
print(x>y)
print(not (x>y))
print(not(x<=y))
print(True and True)
print(True and False)
print(True and False and True)
print(True or False or True)

print(1 and 0)
print(1 and 1)
print((1 and 1) and (1 and 1))
print((1 or 1) or (1 or 1))
print((1 or 1) or (1 or 0))
print((1 or 0) or (1 or 0))
print((1 or 0) or (0 or 0))
print((0 or 0) or (0 or 0))

a,b,c,d=1,1,1,1
print((a or b) and (c or d))
print((a and b) or (c and d))

print(1 ^ 0)
print(1 ^ 1)
print(1 & 1)
print(3 & 2)

print(3 | 2)
'''
print( ~5)
