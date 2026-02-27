# # match case 模式匹配:工作日程安排
#
# day = input("请输入星期(1-7)")
# match day:
#     case "1":
#         print("今天是星期一")
#     case "2":
#         print("今天是星期二")
#     case "3":
#         print("今天是星期三")
#     case "4":
#         print("今天是星期四")
#     case "5":
#         print("今天是星期五")
#     case "6":
#         print("今天是星期六")
#     case "7":
#         print("今天是星期天")
#     case _:
#         print("输入有误")


# 案例 计算机设计 有加减乘除
num1 = float(input("请输入第一个数"))
num2 = float(input("请输入第二个数"))
oper = input("请输入运算符 + - * /")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("输入有误")
