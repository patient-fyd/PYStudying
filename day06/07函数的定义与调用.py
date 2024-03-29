# 函数: 将特定的功能所对应的代码片段进行打包,封存在一个函数内,如果我们想要重复使用该功能,就直接调用函数即可
# 函数的作用: 提高代码复用率,提高开发效率,易于维护

"""
函数定义的格式:
def 函数名(参数1, 参数2,参数3....):
    函数体
    return 返回值

函数调用的格式:
函数名(参数1,参数2,参数3.....)

# 函数名:绝大多数函数都有函数名,没有函数名的函数不能被复用
# 参数:为了让函数灵活性更高,更容易被复用,会动态对函数进行传值,传递的值可以在函数体内部进行使用
# 函数体: 特定功能的代码,写在函数内部,调用函数时可全部执行
# 返回值: 写在return之后,将函数内部计算或运行得到的数据传递到函数体外部
"""


# 定义的时候可以不传参,如果不传调用的时候也不用传参
def run():
    print('我跑的老快了,没人追的上我,钱包在我手里')
    print('我跑的老快了,没人追的上我,手机在我手里')
    print('我跑的老快了,没人追的上我,女朋友在我手里')


# 调用时可以将函数内的代码全部执行一遍
run()
run()
