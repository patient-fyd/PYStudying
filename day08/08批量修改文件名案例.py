# 需求:批量修改指定目录下所有文件的文件名
"""
1.修改时可以通过参数控制是增加,还是删除字符
2.传入指定字符用于增加或者删除
3.使用rename进行重命名
"""

# 导入os模块
import os

# 定义一个控制增加还是删除的变量，true表示增加，false表示删除
flag = True

# 定义一个用于增加或者删除的字符
str1 = 'hello'

# 构造多个文件：文件名为1.txt,2.txt,3.txt,4.txt,5.txt
# for i in range(1,6):
#     # 打开文件
#     f = open('文件夹/'+str(i)+'.txt', 'w')
#     # 关闭文件
#     f.close()


# 定义函数，用于批量修改文件名
def rename_file(flag, str1):
    # 获取当前工作目录
    path = os.getcwd()
    # 获取当前工作目录下的所有文件
    files = os.listdir(path)
    # 遍历所有文件
    for file in files:
        # 判断当前文件是否是文件夹
        if os.path.isdir(file):
            # 如果是文件夹则跳过
            continue
        # 获取文件的后缀名
        ext = os.path.splitext(file)[1]
        # 判断当前文件是否是txt文件
        if ext != '.txt':
            # 如果不是txt文件则跳过
            continue
        # 获取文件的名称
        name = os.path.splitext(file)[0]
        # 判断flag的值
        if flag:
            # 如果flag为true则表示增加
            new_name = name + str1 + ext
        else:
            # 如果flag为false则表示删除
            new_name = name.replace(str1, '') + ext
        # 重命名文件
        os.rename(file, new_name)
