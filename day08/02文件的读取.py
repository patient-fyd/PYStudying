# 文件在'r'模式下可以进行文件读取
# read 可以读取文件

# 打开文件
file = open('python.txt', 'r', encoding='utf-8')

# 读取文件
# n:在read中传入数值,表示读取的字符个数
# 在开发中会给读取数据的值做一个限制,防止文件过大,导致内存溢出，最大读取字符一般为1024*1024
# while True:
#     content = file.read(3)
#     if content == '':
#         break
#     print(content)


# readline 读取一行
# while True:
#     content = file.readline()
#     if content == '':
#         break
#     print(content,end='')


# readlines 读取所有行,返回一个列表
content = file.readlines()
print(content)

# 关闭文件
file.close()
