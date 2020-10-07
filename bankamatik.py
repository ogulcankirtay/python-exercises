ogulcanhesap={
"ad":"oğulcan",
"hesapno":"123465234",
"bakiye":3000,
"ekhesap":2000
}
ahesap={
"ad":"arda",
"hesapno":"123465234",
"bakiye":1000,
"ekhesap":2000
}
def paraCek(hesap,miktar):
    print(f'hoşgeldiniz {hesap["ad"]}')
    if hesap["bakiye"]>=miktar:
        print("paranızı alabilrisiniz: ")
        hesap["bakiye"]=-miktar
    
    elif hesap["bakiye"]+hesap["ekhesap"]>=miktar:
        sorgula=input("bakiyeniz yetmiyor ek hesabı kullanmak istermisiniz (e/h) : ")
        if sorgula =='e':
            a=(miktar-hesap['bakiye'])
            hesap["ekhesap"]=hesap["ekhesap"]-a
            print("paranızı alabilirisiniz:")
            hesap["bakiye"]=0
        else: 
            print(f"hesap bakiye {hesap['bakiye']} ekhesap={hesap['ekhesap']}")
    else:
        print("üzgünüz yetersiz bakiye ve ekhesap:C")

x=int(input(" ne kadar miktar çekmek istiyosunuz: "))

paraCek(ogulcanhesap,x)
print(f"hesap bilgileriniz: {ogulcanhesap}")

