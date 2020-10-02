# sayılar=[1,3,5,7,9,12,19,21]
# # #sayılar dizisini while döngüsü ile yazdırın
# # i=0
# # while i<len(sayılar):   
# #     print(sayılar[i])
# #     i+=1
# # print("bitti ")
# #başlangıc ve bitiş değerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırma
# # i=int(input("başlangıç değeri giriniz: "))
# # x=int(input("bitiş değerini giriniz: "))
# # while i<=x:
# #     if i%2==1:
# #         print(sayılar[i])
# #     i+=1
# # 1 ile 100 arasındaki sayıları azalan bir şekilde yazdırın
# # i=100
# # while i>=0:
# #     print(i)
# #     i-=1
# #kullamıcıdan aldığınız beş sayıyı ekrana sıralı bir şekilde yazdırın
# giris=[]
# i=0
# while i<5:
#     sayı=int(input("sayi giriniz "))
#     giris.append(sayı)
#     i+=1
# giris.sort()
# i=0
# while i<5:
#     print(giris[i])
#     i+=1
#kullanıcıdan alacağınz sınırsız ürün bilgisini ürünler listesinde saklayınız::
ürünler=[]
devam='e'
while devam=='e':
    ürün=input("ürün adı: ")
    fiyat=input("ürün fiyatı: ")
    ürünler.append({
        "ad":ürün,
        "price":fiyat
    })
    devam=input("devam etmek istiyosanız e tuşuna basınız ")
print(ürünler)