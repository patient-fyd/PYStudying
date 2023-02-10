# f-string是python3.6以后退出的格式化方式
name = 'xiaoming'
age = 18
height = 1.85
weight = 69.5
score = 98
id = 7


# 使用f-string进行字符串拼接
# 格式:f'要输出的内容{变量}'
print(F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height}, 学员的体重是{weight}, 学员的分数是{score}%%, 学员的学号是{id}')

# 如果需要调整精度
# {整数型变量:06d} 整型占六位,不足位用0补齐 d可以省略
# {浮点型变量:.2f} 浮点型保留两位小数, 四舍五入
# %可以单独输出
print(F'学员的姓名是{name}, 学员的年龄是{age}, 学员的身高是{height:.2f}, 学员的体重是{weight:.3f}, 学员的分数是{score}%, 学员的学号是{id:06d}')
