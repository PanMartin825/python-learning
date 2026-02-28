# #while循环：打印10遍 MartinGarrix Best DJ ever
#
# DJ = 0
# while DJ < 10:
#     print("MartinGarrix Best DJ ever")
#     DJ += 1
# else:
#     print("Thank you")

#计算1-100之间所有偶数的累加之和
total = 0 # 记录累加之和
num = 1 #循环开始的数字

while num <= 100:
    if num % 2 == 0: #偶数
        total += num
    num += 1
print(f"1-100之间的偶数累加之和:{total}")

