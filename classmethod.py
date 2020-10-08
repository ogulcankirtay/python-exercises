# class Person:
#     # class attributes
#     adress="no information"
#     #constructor(yapıcı metod)
#     def __init__(self,name,bd):
#         #object attributes
#         self.ad=name
#         self.year=bd
#         print("inint metodu çalıştı")
#         #instance method
#     def intro(self):
#         print("hello there"+self.ad)
#         # instance method
#     def calgulateage(self):
#         return 2020-self.year

# p1=Person(name="olcan",bd=1999)
# p2=Person(name="abc",bd=2000)
# p1.intro()
# p2.intro()
# p1.calgulateage()
# p2.calgulateage()
# print(f"p1: adım {p1.ad} yaşım {p1.calgulateage()}")
# print(f"p2: adım {p2.ad} yaşım {p2.calgulateage()}")

class Circle():
    # class object attritubes
    pi=3.14
    #constructor
    def __init__(self,r=1):
        self.r=r
    #methods
    def cevrehesapla(self):
        return 2*self.pi*self.r
    def alanhesapla(self):
        return self.pi*self.r**2
c1=Circle()
c2=Circle(5)
print(f"c1: cevre: {c1.cevrehesapla()} alan: {c1.alanhesapla()}")
print(f"c2: cevre: {c2.cevrehesapla()} alan: {c2.alanhesapla()}")
