names=["ali",'yağmur','hakan','deniz']
years=[1998,2000,1998,1987]
#cenk ismini listenin sonuna ekleyin
# names.append('cenk')

#sena değerini listenin başına ekleyiniz
names.insert(0,'sena')

#deniz ismini listeden siliniz
names.remove("deniz")
print(names)
isa="ali" in names
print(isa)
# kullanıcıdan aldığın 3 tane marka girişini liste ekle
markalar= []
marka=input("marka:")
markalar.append(marka)
marka=input("marka:")
markalar.append(marka)
marka=input("marka:")
markalar.append(marka)
print(markalar)