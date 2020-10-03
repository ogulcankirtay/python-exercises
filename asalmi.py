sayı=int(input("sayi giriniz: "))
asalmı=True
i=0
for i in range(2,sayı):
    if(sayı%i==0):
        asalmı=False
        break
if asalmı:
    print(f"{sayı}: sayı asaldır")
else :
    print(f"{sayı}: sayı asal değildir")