# 什么样的内容可以作为条件出现?
# bool值或者可以转换为布尔值的数据或表达式
# 表达式:经过运算或者执行后,可以得到一个值的代码块或语句都是表达式
# 分支结构,循环结构,赋值,函数定义 不能作为条件出现
# if  a = 1:
#     print('qqwe')
# a = 1
# if if a==1:
#     print()

# 分支语句中只有一个分支的命令会被执行
# 如果运行过程中其中一个条件成立,则后续所有条件不会进行判断
# age = int(input('请输入对方的年龄:'))

# if age > 100 or age < 0:
#     print('数据错误')
# elif age <= 18:
#     print('儿童')
# elif age <= 30:
#     print('青年')
# elif age <= 60:
#     print('中年')
# else:
#     print('老年')

# 练习: 输出小明的评级: 考试分数从0 - 100   优秀(90-100)  良好(80-90)  中等(70-80)  合格(60-70)  不合格(0-60)

score = int(input('请输入小明的成绩:'))

if score > 100 or score < 0:
    print('数据错误')
elif score < 60:
    print('不合格')
elif score < 70:
    print('合格')
elif score < 80:
    print('中等')
elif score < 90:
    print('良好')
else:
    print('优秀')