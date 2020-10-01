# # # sayılar=[1,3,5,7,9,12,19,21]
# # # # sayilar listesindeki üçün katlarını yazdır
# # # # for sayi in sayılar:
# # # #     if sayi%3==0:
# # # #         print(sayi)
# # # #sayilar listesindeki sayıların toplamı kaçtır:
# # # # t=0
# # # # for a in sayılar:
# # # #     t=t+a
# # # # print(t)
# # # # sayilar listesindeki tek sayıların karesini alın:
# # # for a in sayılar:
# # #     if (a%2):
# # #         print(a**2)
# # #şehilerden hangisi en fazla beş karakterlidir
# # şehirler=["rize","kocaeli","konya","izmir","ankara","istanbul"]
# # for a in şehirler:
# #     if (len(a)<=5):
# #         print(a)
# ürünler=[
# {"name":"samsung s6", "price":3000 },
# {"name":"samsung s7", "price":4000 },
# {"name":"samsung s8", "price":5000 },
# {"name":"samsung s9", "price":6000 },
# {"name":"samsung s10", "price":7000 }
# ]
# #ürünlerin toplam fiyatı nedir
# # t=0
# # for urun in ürünler:
# #     t=t+int(urun["price"])
# # print(t)
# # ürünlerden fiyatı en fazla 5000 olan ürünü giriniz:
# for a in ürünler:
#     if(a["price"]<=5000):
#         # print(a["name"])