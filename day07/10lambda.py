# lambda表达式，也叫匿名函数，是一种特殊的函数，它没有函数名，也没有return语句，它的主体是一个表达式，而不是一个代码块。
# lambda表达式的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression

# 需求：根据传入的参数返回最大值 使用lambda表达式
max_num = lambda x, y: x if x > y else y
# 使用变量可以调用lambda表达式
print(max_num(1, 2))


print(type(max_num))  # <class 'function'>


def func():
    print("hello world")


print(type(func))  # <class 'function'>
# 通过type()函数可以看出，lambda表达式和普通函数的类型都是function

# 在使用lambda表达式时，可以不用变量接收，直接调用
print((lambda x, y: x if x > y else y)(1, 2))
# 但只能调用一次，因为lambda表达式没有函数名，所以不能重复调用

# lambda缺点：lambda表达式只能有一个表达式，不适合复杂的逻辑
# lambda表达式不能包含命令，也不能包含多个表达式

# 使用lambda完成递归
# 需求：计算1+2+3+4+5+6+7+8+9+10
# 2.使用lambda表达式
sum_num = lambda num: num if num == 1 else num + sum_num(num - 1)
print(sum_num(10))

# lambda应用场景
# 可以用于一次性函数使用
# 可以作为函数的参数进行传递

# list  sort(key= )
# lsit sort排序方法中的key所需要的参数就是一个函数,我们可以传入lambda表示

list1 = [{'a': 1}, {'b': 12}, {'c': 10}]
# 排序规则:根据字典的第一个键所对应的值进行排序

list1.sort(key=lambda x:list(x.values())[0])
# 格式: 列表.sort(key = lambda 每次传入的元素: 排序所依据的规则)
print(list1)
