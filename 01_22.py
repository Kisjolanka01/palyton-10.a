def f(x:int,y:int)->int:
    """
        f(x,y)=3x+2y
    """
    return 3*x+2*y
print(f(2,3))

print(f(3,2))

f(x=4,y=8)



def ki(x:any):
    print(x)

x=print("szia")
print(x)
if (print("valami")==None):
    print("None-nal tért vissza")



def ki(x:any)->None:
    print(x)
    return 
x=ki("géza")
if x==None:
    print("Nem volt visszatérési érték")

import math as m

def masodfoku(a:float, b:float, c:float):
    """
        Másodfokú megoldóképlet
        return -1 :a=0
        return -2: diszkrimináns < 0
        return int:1 zérushely
        return tuple: 2 zérushely
    """
    if a==0:
        return
    d=b**2-4*a*c
    if d<0:
        return -2
    if d==0:
        return (-b) / (2*a)
    
    x1=(-b+ m.sqrt(d) )/ (2*a)
    x2=(-b- m.sqrt(d) )/ (2*a)

    return x1,x2

x=masodfoku(0,2,1)
if x==-1:
    print("az érték 0 volt")
if x==2:
    print("az")

if type(x)==type(tuple()):
    print("2 zerushelyunk van")

if type(x)==type(tuple()):
    print("kétzérushelyünk van")
print("valami")



class A_NULLA (Exception):
    pass
class DISZKRIMINANS_KISEBB_NULLANAL(Exception):
    pass

def masodfoku_hibadobassal(a:float, b:float, c:float):
    """
        Másodfokú megoldóképlet
        ha a = 0: A_NULLA hiba
        ha a diszkriminans DISZKRIMINANS_KISEBB_NULLANALA hiba
        return -1 :a=0
        return -2: diszkrimináns < 0
        return int:1 zérushely
        return tuple: 2 zérushely
    """
    if a==0:
        raise A_NULLA
    d=b**2-4*a*c
    if d<0:
        raise DISZKRIMINANS_KISEBB_NULLANAL
    if d==0:
        return (-b) / (2*a)
    
    x1=(-b+ m.sqrt(d) )/ (2*a)
    x2=(-b- m.sqrt(d) )/ (2*a)

    return x1,x2

try:
    x=masodfoku_hibadobassal(0,1,2)


except A_NULLA:
    print("az 'a' értéke 0")

except DISZKRIMINANS_KISEBB_NULLANAL:
    print("A diszkriminans kisebb nullanal")





def osszegzes_tetel(l:list):
    """
    osszegzes prog tetel
    return elemek osszege
    """
    s=0
    for i in range(len(l)):
        s+=l[i]
        return s
print(osszegzes_tetel([2,3,4]))






def megszamolas(l:list):
    c=0
for i in range(len(l)):
    if True(l[i]):
        c+=1

print(megszamolas([1,2,34,2,24]))


def maxertek(l:list):
    maxertek=0
    maxindex=0
    for i in range(len(l)):
        if l[i]> maxertek:
            maxertek = l[i]
            maxindex = i
    return maxertek, maxindex
print(maxertek([1,4,62,100]))

def kereses(l:list):
    kszam = int(input("add meg a parameter elejet"))
    kszam = int(input("add meg a parameter veget"))
for i in range(len(l)):
    if l[i]==x:
        return i+1,x
    


