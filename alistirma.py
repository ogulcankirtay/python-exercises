def yazdir(kisilistesi):
    yliste=[]
    for i in kisilistesi:
        yliste.append(i.strip().lower())
    for i in yliste:
        sayi=yliste.count(i)
        if sayi>1:
            print(i)
            for j in range(sayi):
                yliste.remove(i)

kisiler=["mehmet "," Mehmet","meHmet","ahmet","aleyna","merve","Aleyna","halil","Ahmet"]
yazdir(kisiler)