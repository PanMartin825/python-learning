# # 字符串
# # 定义字符串的三种方式
# s1 = "Hello" # 双引号定义
# s2 = 'Python' # 单引号定义
# s3 = """
# Hello:
#     我正在观看并实操Python课程的学习!
# """ # 三引号定义（多行字符串）
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# # 定义字符串 ---> It's very good
# # 转义字符 \' \" \n \t
# msg = 'It\'s very interesting'
# msg2 = "It's my sister"
# msg3 = "Hello 的意思就是 \“您好\”"
# msg4 = "\tI like video games \n\tcome to play with me"
# print(msg)
# print(msg2)
# print(msg3)
# print(msg4)
# print(type(msg))
# print(type(msg2))
# print(type(msg3))
# print(type(msg4))

#字符串拼接
# s1 = "人生苦短" "我用Python"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用Pyhton"
# print("我说："+ msg1 + ","+ msg2)
#
# # 案例:
# name = "PanMartin"
# age = 20
# project = "计算机科学 Ai应用"
# hobby= "电子音乐 电子游戏 程序语言"
# message = ("大家好，我是" + name +"," + "今年" + str(age) + "，" +"正在自考专本和自学学习"+ project +"," "我的爱好是" + hobby + "。" )
# print(message)

# 案例2:%占位符 方式1
# name = "PanMartin"
# age = 20
# project = "计算机科学 Ai应用"
# hobby= "电子音乐 电子游戏 程序语言"
# message = ("大家好，我是%s,今年%s,正在自考专本和自学学习%s,我的爱好是%s." )%(name,age,project,hobby)
# print(message)

# 案例3: f"" 企业开发推荐方式
name = "PanMartin"
age = 20
project = "计算机科学 Ai应用"
hobby= "电子音乐 电子游戏 程序语言"
message = f"大家好，我是{name},今年{age},正在自考专本和自学学习{project},我的爱好是{hobby}."
print(message)


