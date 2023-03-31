# 在函数体内部定义的变量,出了函数体就会被释放掉
def sum1():
    a = 1
    b = 2
    print(a + b)


sum1()
# 思考? 我们再函数体外部可以调用a, b 么?
# NameError: name 'a' is not defined  函数体内部定义的变量,出了函数体救护被释放掉
# print(a + b)

# 全局变量就是在函数体外部书写的一般要在文件内顶格书写,在函数体内部外部都可以调用的变量
a = 1
b = 2


def sum1():
    # 函数体内部可以使用
    print(a + b)


sum1()
# 函数体外部也可以使用
print(a)
print(b)

# for 循环中,  if 分支中创建的变量是全局变量还是局部变量呢? 全局变量
# for i in range(10):
#     pass
#
# print(i)
#
# if True:
#     c = 1
# print(c)


