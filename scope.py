# # # #globale scope 
# # # x="global x"
# # # def funciton(x):
# # #     #local scope
# # #     x="local x"
# # #     print(f"in funciton x = {x}")

# # # funciton(x)
# # # print(f"after fonciton x = {x}")
# # # ################

# # # #global
# # # name="oğulcan"
# # # def chanegename(name):
# # #     name="wwe"
# # #     print(f" in function name={name}")
# # # chanegename(name)
# # # print(f"after function name={name}")
# # # ########333
# # # global string
# # name="glabal string"
# # def greeting(name):
# #     # name="beril"

# #     def hello():
# #         print('heloo '+name)
# #     hello()

# # greeting(name)

# ############3
# ##global yazarak gönderdiğimiz veriyi glabal olarak değiştirebilirz:
# x=100
# def test():
#     global x
#     x=20
# test()
# print(f"x={x}")