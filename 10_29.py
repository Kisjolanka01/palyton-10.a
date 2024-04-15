
def osszegzes_osszeadassal(l:list)-> int:
    """
    osszegzes prog tetel
    return elemek osszege
    """
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s
print(osszegzes_osszeadassal([2,3,4]))


def osszegzes_szorzassal(l:list)-> int:
    
    s=1
    for i in range(len(l)):
        s*l[i]
    return s
print(osszegzes_szorzassal([2,3,4]))



def osszegzes(l:list)-> int:
    """
    osszegzes prog tetel
    return elemek osszege
    """
    s=l[0]
    for i in range(1,len(l)):
        s+=l[i]
    return s
print(osszegzes([2,3,4]))


def megszamlalas(lista:list,condition)->int:
    c=0
    for i in range(len(lista)):
        if condition(lista[i]):
            c+=1
    return c

def paros_e(num:int)->bool:
    return num%2==0
print(megszamlalas([1,2,3,4,5,],paros_e))

print(megszamlalas([1,2,3,4,5,],lambda num: num%2==0))


def szelsoertek_kivalasztas(lista:list,condition):
    index=0
    ertek=lista[0]
    for i in range(len(1,lista)):
        if condition(lista[i],ertek):
            index=i
            ertek=lista[i]
    return index,ertek
def kisebb (num1 ,num2):
    return num1<num2
kisebb_lambda= lambda num1,num2: num1<num2
print(szelsoertek_kivalasztas([2,6,5,3,98,4,-1,5],kisebb))
print(szelsoertek_kivalasztas([2,6,5,3,98,4,-1,5],kisebb_lambda))
print(szelsoertek_kivalasztas([2,6,5,3,98,4,-1,5],lambda num1,num2: num1<num2))


osszeadas=lambda num1,num2: num1<num2

print(osszeadas(2,3))

lista=[2,3,7,6,4,3,2,9]

c=0
otnel_kisebb_e =lambda num:num<5
for i in range(len(lista)):
    if otnel_kisebb_e(lista[i]):
        c+=1
print(c)