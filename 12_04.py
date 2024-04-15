l1= [2,3,4]
l1.append(6)
print(l1[1])
print(len(l1))
l1[2]=10
del l1[2]
print(l1[-1])


l1=[2,3,4,6,12,28]
l2=l1
l2[1]=10
print(l1)
print(l1[1:3])
print(l1[4:])
print(l1[:2])
print(l1[::3])
print(l1[1:5:2])



l=[]
for i in range(10):
    l.append(i**2)



monki=[
    [2,3,3,4],
    [3,4,5,8],
    [3,4,5,10,6]
]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])
