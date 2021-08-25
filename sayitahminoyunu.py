import random
sayi=random.randint(1,100)
tutulansayi=0
print(sayi)
for i in range(1,7+1):
    tutulansayi=int(input("1,100 arası sayiyi tahmin ediniz: "))
    if(sayi==tutulansayi):
        print("bildiniz.")
        break
    else:
        print("tekrar deneyiniz kalan hakkiniz",7-i)
