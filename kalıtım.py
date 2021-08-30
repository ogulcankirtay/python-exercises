class personel():
    def __init__(self,ad,yas,cinsiyet,maas):
        self.ad=ad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.maas=maas
    def bilgileri_yazdir(self):
        return "personelin; ad: {} yas: {} cinsiyet: {} maas {}".format(self.ad,self.yas,self.cinsiyet,self.maas)
p1=personel("ahmet",20,"erkek",10_000)
print(p1.bilgileri_yazdir())
class yonetici(personel):
    def __init__(self,ad,yas,cinsiyet,maas):
        super().__init__(ad,yas,cinsiyet,maas)
    def maas_artir(self,pobject,miktar=1000):
        pobject.maas+=miktar
y1=yonetici("olcan",21,"erkek",15_000)
y1.maas_artir(p1,2500)
print(y1.bilgileri_yazdir())
print(p1.bilgileri_yazdir())