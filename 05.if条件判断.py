# # if案例
# # 正确的账号密码
# ok_account = "PanMartin"
# ok_password = "PanMartin"
# #1. 接收用户输入的账号密码
# account = input("请输入您的账号：")
# password = input("请输入您的密码:")
#
# #
# # #2. 判断账号密码是否全部正确，如果都正确，则登录
# # if account == ok_account and password == ok_password:
# #     print("登录成功，欢迎登录")
# #
# # if account != ok_account and password != ok_password:
# #     print("登录失败，请检查账号密码是否正确")
# # #3. 判断账号密码是否全部正确，如果有任何一个错误，则提示登录失败，提示错误信息
#
# # if... else案例
# # 正确的账号密码
# ok_account = "PanMartin"
# ok_password = "PanMartin"
# #1. 接收用户输入的账号密码
# account = input("请输入您的账号：")
# password = input("请输入您的密码:")
#
#
# #2. 判断账号密码是否全部正确，如果都正确，则登录
# if account == ok_account and password == ok_password:
#     print("登录成功，欢迎登录")
#
# else:
#     print("登录失败,请检查密码是否正确")

# 案例 需求：根据用户输入的年份，判断这一年是闰年还是平年。
year = int(input("请输入要检查的年份:"))
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
   print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")