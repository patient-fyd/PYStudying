# 基础数据类型：int float bool
# 容器类型：str tuple list ser dict

# 整型
int1 = 12
print(type(int1))  # <class 'int'>
# 浮点型
float1 = 12.1
print(type(float1))  # <class 'float'>
# 布尔型
bool1 = True
print(type(bool1))  # <class 'bool'>
# 字符串型
str1 = 'hello python'
print(type(str1))  # <class 'str'>
# 元组
tuple1 = (1, 2, 3, 4)
print(type(tuple1))  # <class 'tuple'>
# 列表
list1 = [1, 2, 3, 4]
print(type(list1))  # <class 'list'>
# 集合
set1 = {1, 2, 3, 4}
print(type(set1))  # <class 'set'>
# 字典
dict1 = {'name': 'ZhangSan', 'age': '18'}
print(type(dict1))  # <class 'dict'>

# python能随时改变变量的数据类型
a = 1
a = 'abc'
a = True