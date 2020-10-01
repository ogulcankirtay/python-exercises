#indexlenemez dizi tipi
fruits={"orange","apple","banana"}
#print(fruits[0]) yapılamaz
# for x in fruits:
# print(x)
fruits.add("cherry")
fruits.update(["mango","grape","apple"]) # bir elemendan birden fazla olmaz o yüzden apple ı yazmayacak

fruits.remove("mango")
print(fruits)
fruits.pop()# normalde son elamanı siler ama burda son eleman diye bişey yok dizi sürekli rasgele yazıldığı için herhangi bi elamnı silinir