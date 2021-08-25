'''def yazdır(sayi,yazi):
    for i in range(sayi):
        print(yazi)
yazdır(10,"nabıyon")
def ebob(sayi1,sayi2):
   ekck=min(sayi1,sayi2)
   eb=1
   for i in range(1,ekck+1):
       if sayi2%i==0 and sayi1%i==0:
           eb =i
   print(eb)
ebob(8,12)
'''
'''
def goster():
    print("selam")
print(type(goster()))
'''
'''
def goster():
    return "selam"
print(goster())
'''
'''
def tekmi_ciftmi(sayi):
    if sayi%2==0:
        return "cift"
    else:
        return "tek"
print(tekmi_ciftmi(5))
'''
'''
def topla(*sayilar):
    toplam=0
    for i in sayilar:
        toplam +=i
    return toplam
print(topla(5,7,6,1,3,8,9))
'''
'''
def kuvvetal(sayi,us=2):
    return sayi**us
print(kuvvetal(3))
print(kuvvetal(3,4))
'''
'''
def degerlerigoster(**degerler):
    for i,j in degerler.items():
        print(i,j)
degerlerigoster(oğulcan="kırtay",renk="yesil",konum="ogrenci")
'''
'''
c=5
def cglobal():
    global c
    c=4
print(c)
cglobal()
print(c)
'''
tekmi= lambda sayi: sayi%2==1
print(tekmi(11))
toplam=lambda *sayilar:sum(sayilar)
print(toplam(1,2,4,5,6))
