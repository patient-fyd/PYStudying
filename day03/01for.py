# for循环的语法结构
"""
for 临时变量 in 数据序列(容器):
    要重复执行的代码
"""
# 循环逻辑:for循环会依次提取数据序列中的元素,每次提取一个,放入临时变量中储存,在循环体中可以使用临时变量,数据序列中有多少个元素,for循环的循环体将会被执行多少次

str1 = 'helloPython'
# 循环遍历str1  遍历:依次提取每一个元素
for i in str1:
    print(i)

# for循环和while循环的区别:
# 1/for循环数据序列,元素提取完成自动停止,不需要使用循环变量
# 2/for循环不需要循环条件,所以也不会有循环条件成立喝不成立的说法
# 3/在开发中我们使用for循环的比例居多,while循环主要是构造死循环结构
# 4/for循环需要配合容器类型(数据序列)进行使用
