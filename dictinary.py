# key -> value
# for example 41->kocaeli 34->istanbul 
#dictinary kullanmadan yapılabilecek hali
# sehirler=["kocaeli","istanbul"]
# plakalar=[41,34]
# print(sehirler[plakalar.index(41)])
#dictinary ile yapımı
# plakalar={'kocaeli' : 41,'istanbul' : 34,'konya' : 42}
# print(type(plakalar))
# print(plakalar['istanbul'])
# print(plakalar["kocaeli"])
users={
"sadıkturan":{
    "age":36,
    'rolls':"user"
   
} ,
"cınarturan":{
    "age":2,
    "rools":["admin","user"]
}
}
print(users["sadıkturan"])
print(users["cınarturan"]["age"])
print(users["cınarturan"]["rools"][0])