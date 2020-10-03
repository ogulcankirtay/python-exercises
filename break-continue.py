# # name="Oğulcan Kırtay"
# # for letter in name:
# #     if (letter==' '):
# #         break
# #     print(letter)
# name='oğulcan kırtay'
# for letter in name:
#     if (letter==' '):
#         continue
#     print(letter)
# x=0
# while x<5:
#     if(x==2):
#         break   
#     print(x)
#     x+=1
# x=0
# # while x<5:
# #     x+=1
# #     if(x==2):
# #         continue   
#     print(x)
# 1 den 100 e kadar tek sayıların toplamını bulunuz:
x=0
t=0
while x<100:
    x+=1
    if(x%2==0):
        continue
    t=x+t
   
print(t)