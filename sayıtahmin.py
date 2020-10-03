import random
sayı=random.randint(1,100)
hak=int(input("kaç hakkınız olsun: "))
can=hak
puan=100
while hak>0:
    hak-=1
    giris=int(input("tahimini sayi griniz: "))
    if giris>sayı:
        puan-=(100/can)
        print("daha küçük")
    elif giris<sayı:
        print("daha büyük bir sayi giriniz: ")
        puan-=(100/can)
    elif giris==sayı:
        print(f"sayiyi buldunuz tebrikler puanınız {puan}:D")
        break
    if hak==0:
        print(f"hakkınız bitti tutulan sayı {sayı}")