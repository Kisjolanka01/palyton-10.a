
import random
eladasok = {
    'het1': [],
    'het2': [],
    'het3': [],
    'het4': [],
}
def feltolt(n):
    for i in range(0,7):
        (n).append(random.randint(0,9))
def osszeg(n):
    sum = 0
    for i in n:
        sum += i
    return(sum)
def uresnap(n):
    sum = 0
    for i in n:
        if i == 0:
            sum += 1
    return(sum)
def paratlan(n):
    sum = 0
    for i in n:
        if i%2==1:
            sum +=1
    return (sum)
feltolt(eladasok['het1'])
feltolt(eladasok['het2'])
feltolt(eladasok['het3'])
feltolt(eladasok['het4'])
teljes = osszeg(eladasok['het1'])
teljes += osszeg(eladasok['het2'])
teljes += osszeg(eladasok['het3'])
teljes += osszeg(eladasok['het4'])
print ('Osszesen', teljes, 'kokuszgolyot adtunk el.')
print('Az elso heten', osszeg(eladasok['het1']), 'kokuszgolyo volt.')
print('Az masodik heten', osszeg(eladasok['het2']), 'kokuszgolyo volt.')
print('Az harmadik heten', osszeg(eladasok['het3']), 'kokuszgolyo volt.')
print('Az negyedik heten', osszeg(eladasok['het4']), 'kokuszgolyo volt.')
if osszeg(eladasok['het1']) > osszeg(eladasok['het2']) and osszeg(eladasok['het1']) > osszeg(eladasok['het3']) and osszeg(eladasok['het1']) > osszeg(eladasok['het4']):
    print('Az elso heten volt a legtobb eladott kokuszgolyo.')
elif osszeg(eladasok['het2']) > osszeg(eladasok['het1']) and osszeg(eladasok['het2']) > osszeg(eladasok['het3']) and osszeg(eladasok['het2']) > osszeg(eladasok['het4']):
    print('Az masodik heten volt a legtobb eladott kokuszgolyo.')
elif osszeg(eladasok['het3']) > osszeg(eladasok['het2']) and osszeg(eladasok['het3']) > osszeg(eladasok['het1']) and osszeg(eladasok['het3']) > osszeg(eladasok['het4']):
    print('Az harmadik heten volt a legtobb eladott kokuszgolyo.')
elif osszeg(eladasok['het4']) > osszeg(eladasok['het2']) and osszeg(eladasok['het4']) > osszeg(eladasok['het1']) and osszeg(eladasok['het4']) > osszeg(eladasok['het3']):
    print('A negyedik heten volt a legtobb eladott kokuszgolyo.')
ures = uresnap(eladasok['het1'])
ures += uresnap(eladasok['het2'])
ures += uresnap(eladasok['het3'])
ures += uresnap(eladasok['het4'])
print (ures, 'Ures nap volt.')
if paratlan(eladasok['het1']) < paratlan(eladasok['het2']) and paratlan(eladasok['het1']) < paratlan(eladasok['het3']) and paratlan(eladasok['het1']) < paratlan(eladasok['het4']):
    print('Az elso heten volt a legkevesebb paratlan eladas.')
elif paratlan(eladasok['het2']) < paratlan(eladasok['het1']) and paratlan(eladasok['het2']) < paratlan(eladasok['het3']) and paratlan(eladasok['het2']) < paratlan(eladasok['het4']):
    print('Az masodik heten volt a legkevesebb paratlan eladas.')
elif paratlan(eladasok['het3']) < paratlan(eladasok['het2']) and paratlan(eladasok['het3']) < paratlan(eladasok['het1']) and paratlan(eladasok['het3']) < paratlan(eladasok['het4']):
    print('Az harmadik heten volt a legkevesebb paratlan eladas.')
elif paratlan(eladasok['het4']) < paratlan(eladasok['het2']) and paratlan(eladasok['het4']) < paratlan(eladasok['het1']) and paratlan(eladasok['het4']) < paratlan(eladasok['het3']):
    print('A negyedik heten volt a legkevesebb paratlan eladas.')