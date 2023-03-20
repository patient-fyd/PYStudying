# 什么是字符串索引?
# 就是保存字符串时,将所有字符依次存入字符串所在空间,并且按照顺序将元素依次存放, 为了方便存取数据,我们讲元素进行编号,从0开始依次递增
# 通过下标索引,可以获取元素,或者进行切片等操作

str1 = 'helloworld'
# 通过索引获取元素的格式:  字符串[元素索引]
# 需求:想获取第5个元素
print(str1[4])
# 需求:获取e
print(str1[1])

'''
h  e  l  l  o
# 正数索引
0  1  2  3  4
# 负数索引
-5 -4 -3 -2 -1
'''
# 结论:字符串中的索引,正数索引从0开始,从左至右依次递增, 负数索引,从-1开始从右至左依次递减
# 需求:使用负数索引取 r
print(str1[-3])
