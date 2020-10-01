numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
#dizideki en küçük elemanı verir
val=min(numbers)
print(val)
val=min(letters)
print(val)
#dizideki max elemanı verir
val=max(numbers)
print(val)
val=max(letters)
print(val)
# dizinin sonuna eleman ekleme
numbers.append(49)
numbers.append(59)
print(numbers)
# belirtilen indexe eleman ekleme
numbers.insert(3,78)
numbers.insert(-1,52)
# .pop() istediğimiz indexi giriptede silebiliriz girmezsek son elemanı siler
numbers.pop()
numbers.pop(0)
# .remove silmekten istediğimiz karakteri buup siler
numbers.remove(49)
# .sort sayısal büyüklük olarak sıralanır küçükten büyük
numbers.sort()
letters.sort()
#tersine çevirmek 
numbers.reverse()
#tüm elemanları silmek iiçin
numbers.clear()