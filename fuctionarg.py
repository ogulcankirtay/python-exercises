# # # def changename(n):
# # #     n="abdi"

# # # name="safa"
# # # changename(name)
# # # print(name)
# # # #burda adres gönderdiğimiziçin değişiyo dipğerlerinde kopyasını gönderiyoduk
# # # def change(n):
# # #     n[0]="istanbul"
 
# # # sehirler=["anraka","izmit"]
# # # #slicing ile dizinin kopyasını gönderecez
# # # change(sehirler[:])
# # # print("slicing yöntemiyle gönderilen fonksiyon: ",sehirler)
# # # print(f"fonksiyondan önce  {sehirler}")
# # # change(sehirler)
# # # print("fonksiyondan sonra")
# # # print(sehirler)
# # #sınırsız sayıda bu şekilde parametre yazılabilir am daha kolay bir yolu var
# # # def add(a,b,c=0):
# # #     return sum((a,b,c))
# # # print(add(10,10,30))
# # #kolay yolu parametrenin başına * koyduğunda istediğin kadar veri gönderebilirsin gönderdiğin bu veriler tuple şeklinde depolanır
# # def add(*params):
# #     print(params)
# #     print(type(params))
# #     return sum((params))

# # print(add(10,20,30,40,50))
# #key value fonkisyonları gönderimi
# def displayuser(**params):
#     for key,value in params.items():
#         print(f"{key} is {value}")
#     print(params)

# displayuser(name="oğulcan",age=21,phone=12334,email="ogulcan@gmail.com")
# displayuser(name="abdi",age=34,city="izmir")
# displayuser(name="faruk",age=30,city="izmit",phone="2345",email="abdilifaruk@gmail.com")
def myfunc(a,b,*arg,**kwargs):
    print(a)
    print(b)
    print(arg)
    print(kwargs)

myfunc(1,3,4,5,6,7,key1="value1",key2='value2')