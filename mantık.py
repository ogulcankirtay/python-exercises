from os import kill
"""""
a=True
b=False
print(type(a))
a=0
b=1
print(bool(a))
print(bool(b))
esitmi="selam"=="naber"
print("esitmi " +str(esitmi))

kullanici=["ogulcan@gmail.com","1234567890"]
kadi=input("kullaniciadini giriniz: ")
sifre=input("sifre giriniz: ")
if kadi==kullanici[0] and sifre==kullanici[1]:
    print("hosgeldiniz",kullanici[0])
else:
    print("yanlis sifre veya kullanici adi")
"""
ad=input("ogrenci adini giriniz: ")
vize=float(input("vize notunu giriniz: "))
final=float(input("final notunu giriniz: "))
ort=(vize*0.4)+(final*0.6)
if ort>=85:
    harf_not="AA"
elif ort>=70:
    harf_not = "BA"
elif ort>=60:
    harf_not = "BB"
elif ort>=50:
    harf_not = "cb"
elif ort>=40:
    harf_not = "CC"
else:
    harf_not = "FF"
print(ad,"adli ogrencinin genel ortalamasi",ort,"harfnotu",harf_not)
with open("notlar.txt","w") as dosya:
    dosya.writelines("{} : {} {} ".format(ad,ort,harf_not))