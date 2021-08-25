'''sayilar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(type(sayilar))
for i in sayilar:
    print(i)
list_1=[(1,2),(3,4),(5,6)]
print(list_1)
for x,y in list_1:
    print(x,y)


a=10
while(a>0):
    print(a)
    a-=1
liste=[1,2,"oğulcan",4,"kırtay",True]
for i in liste:
    print(i)
uzunluk=len(liste)
sayac=0
while sayac<uzunluk:
    print(liste[sayac])
    sayac+=1

# yazı tura
import random
list=["tura","yazi"]
t_sayisi=0
y_sayisi=0
adet=int(input("kaç kere atmak istiyosunuz: "))
while adet>0:
    tur=random.choice(list)
    if tur=="tura":
        t_sayisi+=1
    else:
        y_sayisi+=1
    adet-=1
print("tura sayisi: {} yazi sayisi: {}".format(t_sayisi,y_sayisi))

for i in range(101):
    print(i)
for i in range(20,100,2):
    print(i)

sonsayi=int(input("son rakamı giriniz: "))
asalmi=False
for sayi in range(2,sonsayi):
    if sonsayi%sayi!=0:
        asalmi=True
    else:
        asalmii=false
        break

if(asalmi==True):
    print(sonsayi,"asaldir")

while True:
    a=int(input("tek sayi girerseniz sonlanır aksi takdirde devam eder:"))
    if a%2==0:
        print("devamediyo")
    else:
        break
print("döngü sonlandı:")

while True:
    a=int(input("tek sayı girerseniz ekranda gözükmeyecektir:"))
    if a%2:
        continue
    print(a)
'''