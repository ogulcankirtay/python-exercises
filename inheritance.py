# İnheritance (KALITIM) : Miras alma
# Person => name,lastname,age ,eat(),run(),drink()
#Student(Person),Teacher(Person)
# Animal=> Dog(Animal),Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("Person created")
    def whoAmİ(self):
        print("I am a Person")
    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number=number
        print("student created")
    # OVERRİDE
    def whoAmİ(self):
        print("I am a student")
    def sayhello(self):
        print("hello ı am student")
class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch
    def whoAmİ(self):
            print("ı am a teacher")
p1=Person("oğulcan","kırtay")
s1=Student("ali","vural",1234)
t1=Teacher("sadık","yılmaz","math")
print(p1.firstname+" "+p1.lastname)
print(s1.firstname+" "+s1.lastname+" "+str(s1.number))

p1.whoAmİ()
s1.whoAmİ()
p1.eat()
s1.eat()
s1.sayhello()
t1.whoAmİ()
