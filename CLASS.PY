#CLASS
class Person:
    #class attributes
    # pass yyazabiliriz hata almamak için veya
    adress="no information"
    # contsructor(yapıcı method)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.bday=year
        print("init metodu çalıştı")
        # methods

# object(instance)
p1=Person("oğulcan",1999)
p2=Person("beril",2005)
# updating
# p1.name="abc"
# p1.adress="kocaeli"
# accesing object attributes
print(f"p1: name: {p1.name} year:{p1.bday} aderess: {p1.adress}")
print(f"p2: name: {p2.name} year:{p2.bday} ")
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)