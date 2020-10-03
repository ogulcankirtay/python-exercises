# # # # # # # # # # girilen aralığa göre sayıları item değişkenine atadık teker teker 
# # # # # # # # # for item in range(10):  
# # # # # # # # #     print(item)
# # # # # # # # for item in range(50,100):
# # # # # # # #     print(item)
# # # # # # # # for item in range(50,100,10):
# # # # # # # #     print(item)
# # # # # # # # print(list(range(5,20,5)))
# # # # # # # #enumerate
# # # # # # # # greting='hello'
# # # # # # # # for item in enumerate(greting):
# # # # # # # #     print(item)
# # # # # # # # a="hello"
# # # # # # # # for index,item in enumerate(a):
# # # # # # # #     print(item)
# # # # # # # #     
# # # # # # # a="hello"
# # # # # # # for index,item in enumerate(a):
# # # # # # #     print(index)
# # # # # # # a="hello"
# # # # # # # for index,item in enumerate(a):
# # # # # # #     print(item,index)
# # # # # # # zip
# # # # # # # list1=[1,2,3,4,5]
# # # # # # # list2=["a","b","c","d","e"]
# # # # # # # print(list(zip(list1,list2)))
# # # # # # list1=[1,2,3,4,5]
# # # # # # list2=["a","b","c","d","e"]
# # # # # # list3=["100","200","300","400","500"]
# # # # # # print(list(zip(list1,list2,list3)))
# # # # # # list1=[1,2,3,4,5]
# # # # # # list2=["a","b","c","d","e"]
# # # # # # list3=["100","200","300","400","500"]
# # # # # # for item in zip(list1,list2,list3):
# # # # # #      print(item)
# # # # # list1=[1,2,3,4,5]
# # # # # list2=["a","b","c","d","e"]
# # # # # list3=["100","200","300","400","500"]
# # # # # for a,b,c in zip(list1,list2,list3):
# # # # #      print(a,b,c)
# # # # numbers=[]
# # # # for x in range(10):
# # # #     print(x)
# # # # numbers=[x for x in range(10)]
# # # # print(numbers)
# # # # numbers=[x**2 for x in range(10) if x%3==0]
# # # # print(numbers)
# # # mystring='hello'
# # # mylist=[]
# # # for letter in mystring:
# # #     mylist.append(letter)
# # # print(mylist)
# # # #basit yolu
# # # mylist=[letter for letter in mystring]
# # # print(mylist)
# # years=[1975,1972,1999,2005]
# # ages=[2020-a for a in years]
# # print(ages)
# # result=[x if x%2==0 else 'tek' for x in range(1,10)]
# # print(result)
# result=[]
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)
# result=[(x,y) for x in range(3) for y in range(3)]
# print(result)
# result=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
# print(result)
