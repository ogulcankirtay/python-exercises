from random import choice
class mp3calar():
    def __init__(self,sarkilistesi=[]):
        self.suanCalanSarki=""
        self.ses=100
        self.sarkilistesi=sarkilistesi
        self.durum=True
    def SarkiSec(self):
        i = 0
        for sarki in self.sarkilistesi:
            print("{} {}".format(sarki, i))
            i += 1
        secilenSarki = int(input("secmek istediğiniz şarkının indeksini giriniz: "))

        while secilenSarki < 0 or secilenSarki > len(self.sarkilistesi) - 1:
            secilenSarki = int(input("yanlış seçim \nsecmek istediğiniz şarkının indeksini giriniz: "))
        self.suanCalanSarki = self.sarkilistesi[secilenSarki]


    def SesArtir(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10


    def SesAzalt(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10


    def RastgeleSarkiSec(self):
        rssec=choice(self.sarkilistesi)
        self.suanCalanSarki=rssec
    def SarkiEkle(self):
        sanatci = input("sanatçı/grubu giriniz: ")
        sarki = input("sarkiyi giriniz")
        self.sarkilistesi.append(sanatci + " - " + sarki)
    def SarkiSil(self):
        i = 0
        for sarki in self.sarkilistesi:
            print("{} {}".format(sarki, i))
            i += 1
        silineceksarki = int(input("silenecek şarkının indeksini giriniz: "))

        while silineceksarki < 0 or silineceksarki > len(self.sarkilistesi) - 1:
            silineceksarki = int(input("yanlış seçim \nsilenecek şarkının indeksini giriniz: "))
        self.sarkilistesi.pop(silineceksarki)
        # self.sarkilistesi.remove(self.sarkilistesi[silineceksarki])
    def Kapa(self):
        self.durum=False
    def MenuGoster(self):
        print("""
        Şarkı listesi: {}
        ŞUan Çalan Şarkı: {}
        Ses Duzeyi: {}
        1- Şarkı Seç
        2-Ses Artır
        3-Ses Azalt
        4-Rastgele Şarkı Seç
        5-Şarkı Ekle
        6-Şarkı Sil
        7-Kapa     
        """.format(self.sarkilistesi,self.suanCalanSarki,self.ses))
    def secim(self):
        sec=int(input("Seçimizi Giriniz: "))

        while sec<1 or sec>7:
            sec=int(input("Yanlış Seçim (1-7) Seçimizi Giriniz: "))
        return sec

    def calistir(self):
        self.MenuGoster()
        sec=self.secim()

        if sec==1:
            self.SarkiSec()
        if sec==2:
            self.SesArtir()
        if sec==3:
            self.SesAzalt()
        if sec==4:
            self.RastgeleSarkiSec()
        if sec==5:
            self.SarkiEkle()
        if sec==6:
            self.SarkiSil()
        if sec==7:
            self.Kapa()

Mp3calar=mp3calar()
while Mp3calar.durum:
    Mp3calar.calistir()
print("bitti")