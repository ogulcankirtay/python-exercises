'''def reverse_int(sayi):
    basamakdegerleri=[]
    while sayi>1:
        basamakdegerleri.append(int(sayi%10))
        sayi/=10
    print(basamakdegerleri)

reverse_int(1234)
'''
def reverse_int(sayi):
    return int(str(sayi)[::-1])
print(reverse_int(1234))
