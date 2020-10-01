# numbers=[1,2,3,4,5]
# for a in numbers: # burdaki a değişken istediğini yazabilirsin
#     print(a)
#     print("merhaba")
# tupple=(1,2,3,4,5)
# for t in tupple:
#     print(t)
# lt=[(1,2),(1,3),(1,4),(1,5)]
# for a in lt:
#     print(a)
# for a,b in lt:
#     print(a,b)
# #     print(b)
# d={"k1":1,
# "k2":2,
# "k3":3}
# for item in d:
#     print(item) # sadece keyleri yazar 
# d={"k1":1,
# "k2":2,
# "k3":3}
# for item in d.items():
#      print(item)
d={"k1":1,
"k2":2,
"k3":3}
for key,value in d.items():
     print(key,value)