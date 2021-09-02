'''dosya=open("planlar.txt","r",encoding="utf-8")
#print(dosya.read(5))
#print(dosya.readline())
#print(dosya.readlines())
print(dosya.read(21))
print(dosya.tell())
print(dosya.seek(10))
print(dosya.tell())
dosya.close()
'''

#dosya=open("planlar.txt","w",encoding="utf-8")
#dosya.write("merhaba arkadaşlar")
#dosya=open("planlar.txt","a",encoding="utf-8")
#dosya.write("selam")
#dosya.close()
with open("planlar.txt","a",encoding="utf-8") as dosya:
    dosya.write("\nselamla")
