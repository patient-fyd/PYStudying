# 格式: '字符串,占位符' % 变量
# 在上述格式中,格式化完成后,会将占位符位置填充上对应的变量
# 不同数据类型的变量,要使用不同的占位符进行占位

# 字符串数据使用 %s
# 浮点型数据使用 %f
# 整型数据使用   %d

name = 'xiaoming'
age = 18
height = 1.85
weight = 69.7
marriage = False
id = 123

# 一个占位符的格式化输出
print('姓名是 %s' % name)
print('年龄是 %d' % age)
print('身高是 %f' % height)
print('体重是 %f' % weight)
print('婚姻状况是 %s' % marriage)


print('姓名是%s, 年龄是%d岁, 身高是%f米, 体重是%fkg, 婚姻状况是%s' % (name, age, height, weight, marriage))


# 需求:1.身高保留两位小数,体重保留三位小数
# 需求:2.学员的id共占用6位,不足位用0填充

# 浮点型保留n位小数: %.nf
# 整型占用n位数据,不足位用0补齐  %0nd
print('学员的姓名是%s, 学员的年龄是%d岁, 学员的身高是%.2f米, 学员的体重是%.3fkg, 学员的编号是%06d' % (name, age, height, weight, id))