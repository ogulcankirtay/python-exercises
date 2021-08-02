#list derlseri
a =list()
b=[]
print("type a ",type(a))
print("type b ",type(b))
ogrenciler=["ali","veli","vedat","ayşe","selma","eda","gamze","ahmet"]
print("ogrenci[3]",ogrenciler[3])
"""
# döngü içinde 
for ogrenci in ogrenciler:
    print(ogrenci)
"""
"""
# fonksiyonel işlemler 
print(len(ogrenciler))
ogrenciler.remove("ali")
print(ogrenciler)
print(len(ogrenciler))
"""
print("ilk 3 eleman",ogrenciler[:3])
ogrenciler[2]="vehdat"
print(ogrenciler[::-1])