
int1 = 12
float1 = 14.9
str1 = '12'
str2 = '14.3'
str3 = 'python'

# 数据类型转换的细节
# int   float  str类型之间的转换
# int >> float
# int类型转换为float类型将会在整数末尾加.0
print(float(int1))
print(type(float(int1)))

# float >> int
# float转换为int类型,将会将小数部分去除,只保留整数部分
print(int(float1))

# int >> str
# int类型可以随意转换为str类型,但是输出结果不发生改变,转化为str类型后可以使用str类型的各种函数
print(str(int1))

# str >> int
# 字符串中是int类型数据,可以转换为int类型
print(int(str1))
# ValueError: invalid literal for int() with base 10: '14.3'
# 字符串中是float类型数据,不可以转换为int类型
# print(int(str2))
# ValueError: invalid literal for int() with base 10: 'python'
# 字符串中是字符型数据,不可以转换为int类型
# print(int(str3))

# float >> str
# float类型可以随意转换为str类型,但是输出结果不发生改变,转化为str类型后可以使用str类型的各种函数
print(str(float1))

# str >> float
# 字符串中是int类型数据,则可以转换为float类型数据,并且在末尾加.0
print(float(str1))
# 字符串中是float类型数据,可以转换为float类型数据
print(float(str2))
# ValueError: could not convert string to float: 'python'
# 字符串中是字符型数据则不能转换为float类型数据
print(float(str3))