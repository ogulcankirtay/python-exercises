# # #gönderilen bir kelimeyi belirtilen kez output veren fonksiynnu yazınız:
# # # def write(n,word):
# # #     x=0
# # #     while n>x:
# # #         x+=1
# # #         print(word)
# # # n=int(input("kaç kez yazılsın: "))
# # # word=input("girmek istediğiniz kelimeyi giriniz: ")
# # # write(n,word)
# # #kendine gönderilen sınırsız sayıdaki paramtereyi bir listeye çeviren fonksiyon
# # def convertlist(*params):
# #     list=[]
# #     for item in params:
# #         list.append(item)

# #     return list
# # a=convertlist(10,20,"a",50)
# # print(a)
# # gönderilen iki sayı arasındaki tüm asal sayı bulan fonksiyon
# a=int(input("başlangıc griniz:"))
# b=int(input("bitiş giriniz: "))
# def asalmi(a,b):
#     for sayi in range(a,b+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if sayi%i==0:
#                     break
#             else :
#                 print("sayi asal ",sayi)
# asalmi(a,b)
#kendine gönderilen sayının tam bölenlerini bir liste halinde dönderen fonksiyon
def tambölen(sayi):
    list=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            list.append(i)
    return list
sayi=int(input("sayi giriniz: "))
a=tambölen(sayi)
print(a)
