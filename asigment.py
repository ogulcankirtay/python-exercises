# # x=5
# # y=6
# # z=4
# # x,y,z=5,6,4
# # x+=5
# # y-=5
# # z*=4
# # x%=2
# # y//=2
# # z/=3
# # values=1,2,3,4,5
# # x,y,*z=values
# # # print(x,y,z)
# # a,b,c,d=5,5,6,7
# # result=(a==b) #parnatezler okunurluk açısından kondu istersen koyma True
# # print(result)
# # username='ogulcank'
# # pasword=1234
# # result=("ogulcank"==username)
# # print(result)
# # result=(pasword!=1234)
# # # print(result)
# # a,b,c=5,6,7
# # result=a>=8
# # print(f"a>=8 {result}")
# # result=b<c
# # print(f"b<c {result}")
# # x=5
# # result=5<=x<=10
# # print(result)
# # and ve operatörü
# # #and operatörü için karşılaştırmalardan herhangi birisi ynalışsa tamamı yanlış hepsi doğruysa doğru
# # x=6
# # devam='e'
# # result=(x<5) and (devam=='e')
# # print(result)
# # #or yada operaötü için herhangi birisi doğruysa doğru hepsi yanlışsa yanlış
# # x=4
# # result=((x>0) or (x%2==0))
# # result=(x>3) or (x==0)
# # print(result)
# # # not 
# x=4
# result=not(x<0)
# print(result)

# # is adreslerinin aynı olup olmadığına bakıyo
# x=y=[1,2,3]
# z=[1,2,3]
# result=x is y
# print(result)
# result=x is z
# print(result)
# #in  listenin elemenaı mı değil  i ona bakıyo
x=["apple","banana"]
result=("banana" in x)
print(result)