'''
import sys
filename=sys.argv[1]
def filebeolLista(filename):
    f=open(filename)
    sorok=f.readlines()
    f.close()
    atalakitott=atalakitas(sorok)
    return atalakitott
'''

l=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

'''
def maxkivkedd(matrix):
    oszlop=1
    maxertek=matrix(0)[oszlop]
    maxsor=0
    for i in range(1,len(matrix)):
        if maxertek<matrix[i][oszlop]:
            maxertek=matrix[i][oszlop]
            maxsor=i
    print(F"legtobb{matrix} helye {maxsor}")
'''

nevek=[Alex,Szandi,Gaspar]


def sorosszeg(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
        return s

def maxsorosszeg(matrix):
    maxertek=sorosszeg(matrix[0])
    maxindex=0
    for i in range(1,len(matrix)):
        if maxertek<(sorosszeg[matrix[i]]):
            maxertek=(sorosszeg[matrix[i]])
            maxindex=i
            return maxindex,maxertek
        index,max=maxsorosszeg(l)
        print(f"{nevek} ennyit keszitett a heten{max}")



