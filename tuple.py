#tuple
from builtins import tuple

a=()
b=tuple()
print("type a",type(a),"type b",type(b))
a=(1,2,4,5,6,7)
print(a)
print(a[1])
#a[1]=1 ->tuple da değer ataması yapılmaz
yazi="selam nası gidiyo  "
yeniyazi=tuple(yazi)
print(yeniyazi)
print(yeniyazi.index("l"))
print(yeniyazi.count(" "))
print(yeniyazi.__contains__("x")) # x elemeanını bulundurmuyor