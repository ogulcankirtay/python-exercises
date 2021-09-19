'''def move_to_zero(liste):
    for i in liste:
        sayi=liste.count(0)
        for j in range(sayi):
            liste.remove(0)
        for j in range(sayi):
            liste.append(0)
    print(liste)
move_to_zero([1,2,0,3,0,4,10,0,5,9])
'''
def move_to_zero(liste):
    for i in liste:
        if i==0:
            liste.remove(0)
            liste.append(0)
    print(liste)
move_to_zero([1,2,0,3,0,4,10,0,5,9])