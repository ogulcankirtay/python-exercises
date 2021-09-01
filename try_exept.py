'''while True:
    try:
        boy=float(input("boyunuzı metre cinsinden giriniz(örnek:1.78): "))
        break
    except:
        print("lütfen doğrı giriş yapınız: ")
while True:
    try:
        kilo=float(input("lütfen kilonuzu kg cinsinden giriniz(78.5):"))
        break
    except:
        print("lütfen doğrı giriş yapınız: ")

print("kilo indeksiniz: ",kilo/boy**2)

'''
def sayitopla(sayilar):
    sayi=0
    if type(sayilar)!=list:
        raise TypeError("Parametre list objesi olmalı")
    for i in sayilar:
        sayi+=i
    return sayi
try:
    print(sayitopla([1,2,3,4]))
except:
    print("buraya girdi:D")