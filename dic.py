sözlük= dict()
sözlük={}
print(type(sözlük))
kisiler={"melis":20,
         "mahmut":19,
         "ali":40,
         1:"al"}
print("melis:",kisiler["melis"])
print(kisiler)
uyeler={"uye" : ["ali","veli","ahmet"],
        "moderatör" : ["memet","halil"],
        "yoneticiler" : ["salih","can","onur"]}
uyeler["smoderetörler"]=["defne","derin"]
print(uyeler)
uyeler["uye"].append("hamit")
print(uyeler["uye"])
uyeler["yoneticiler"].remove("onur")
print(uyeler["yoneticiler"])