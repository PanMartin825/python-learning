# for 循环 遍历输入的字符串
#
# msg = input("请输入需要遍历的字符串:")
#
#  for s in msg:#s 表示遍历出来的元素；msg 表示需要遍历的数据
#    print(f"元素 ： {s}")
# else:
#      print("遍历结束")
#
#  基于for循环完成如下需求
#  1．计算1-100之间所有奇数之和。
# #2．计算100-500之间所有3的倍数的数字之和
# 原始写法
# total = 0
#  for i in range(1,101):
#     if i % 2 == 1:
#       total = total + i
#  print(total)
#
#  简化
# total = 0
# for i in range(1,101,2):
#        total = total + i
# print(total)
#
# total = 0
# for i in range(100,501):
#  if i % 3 == 0:
#        total = total + i
# print(total)

# 打印长方形

#1. 接受键盘录入 m,n # print自带换行效果
m = int(input("请输入长度"))
n = int(input("请输入宽度"))
for j in range(n):
 for i in range(m):
    print("*",end="  ")
 print()