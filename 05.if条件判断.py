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
# year = int(input("请输入要检查的年份:"))
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#    print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

#if...elif...else案例：根据用户输入的数字，判断数字是正数，还是负数，还是0
# num = int(input("请输入数字:"))
# if num > 0:
#     print("该数字是正数")
# elif num < 0:
#     print("该数字是负数")
# else:
#     num = 0
#     print("该数字是0")

# 1，根据输入用户名、密码进行登录系统。
# 用户名、密码为admin/666888或root/547527或zhangsan/123456，则输出登录成功
# # 否则就提示用户名或密码错误
# user1 = "admin"
# user2 = "root"
# user3 = "zhangsan"
# pass1 = "666888"
# pass2 = "547527"
# pass3 = "123456"
# username = input("请输入账号:")
# password = input("请输入密码:")
# if username == user1 and password == pass1:
#     print("登陆成功")
# elif username == user2 and password == pass2:
#     print("登陆成功")
# elif username == user3 and password == pass3:
#     print("登陆成功")
# else:
#     print("登录失败，用户名或密码错误")

"""
# 案例：三角形类型判断：根据输入的三个边的边长（正整数)，判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
1，构成三角形的条件：两边之和大于第三边
2．三角形判定规则
三个边都相等：等边三角形
两个边相等：等腰三角形
三个边都不相等：普通三角形
"""
#1，接收输入的三角形三个边的边长
a = int(input("请输入边长"))
b = int(input("请输入边长"))
c = int(input("请输入边长"))

# 2. 判断三角形的类型
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print(f"{a}{b}{c}三个边长是等边三角形")
    elif a == b or b == c or a == c:
        print(f"{a}{b}{c}三个边长是等腰三角形")
    else:
        print("这三个边长能构成普通三角形")

else:
    print("这三个边长不能构成三角形")