cars=['bmw','mercedes','opel','mazda']
print(cars)
print(f"carsın boyutu {len(cars)}")
print(f"listin ilk elemeanı {cars[0]} listenin son elemanı {cars[len(cars)-1]}")
cars[len(cars)-1]="toyata"
print(cars[len(cars)-1])
# mercedes carsın bir elemanı mıdır
result="mercedes" in cars
print(result)
#son iki elemanını değiştir
cars[-2:]=["renault","nissan"]
print(cars)
cars=cars+["audi","ford"]
print(cars)
#listenin son elemanını silin
del cars[-1]
print(cars)
#diziyi tersten yazdırma
print(cars[::-1])
#Aşağıdaki verileri bi list içine saklayın
#  studenta: Yiğit Bilgi 2010 [70,60,70]
#studentb: sena turan 1999 [80 80 70]
#studentc : AHMET TURAN 1998 [80,70,90]
STUDENTS=[["Yiğit","Bilgi",2010,[70,60,70]],["Sena","Turan",1999,[80,80,70]],["ahmet","turan",1998,[80,70,90]]]
print(STUDENTS[1])