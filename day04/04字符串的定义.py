# 字符串的定义方式
# 单引号
str1 = 'hello world'
# 双引号
str2 = "hello python"
# 三对单引号
str3 = '''hello 3333'''
# 三对双引号
str4 = """hello 4444"""

# 一对引号和三对引号的区别
# 在一对引号内部进行手动换行，打印的时候无法换行
str1 = 'hello'\
    'world'
print(str1)
# 在三对引号内部手动换行，打印的时候输出换行格式
str3 = '''hello
world'''
print(str3)