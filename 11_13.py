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