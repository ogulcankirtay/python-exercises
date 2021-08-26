class araba():
    def __init__(self,mrk,mdl,fyt,rnk):
        self.marka=mrk
        self.model=mdl
        self.fiyat=fyt
        self.renk=rnk
    def bilgiyazdir(self):
        print(self.marka,self.model,self.fiyat,self.renk)
    def fiyatdegistir(self,fyt):
        self.fiyat=fyt
Araba1=araba("renoult","clio",20_000,"kırmızı")
Araba1.bilgiyazdir()
Araba2=araba("ford","mustang",500_000,"siyah")
Araba2.bilgiyazdir()
Araba2.fiyatdegistir(600_000)
Araba2.bilgiyazdir()
