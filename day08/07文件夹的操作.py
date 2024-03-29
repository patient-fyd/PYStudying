# 在使用下方函数或方法时,需要先导入os模块方可使用
import os
# mkdir 创建文件夹
# FileExistsError: [Errno 17] File exists: 'student'
# 如果创建的文件夹已经存在则报错
# os.mkdir('student')
# 可以在已经存在的文件夹下创建文件夹
# os.mkdir('文件/students')
# FileNotFoundError: [Errno 2] No such file or directory: 'aaa/bbb'
# os.mkdir('aaa/bbb')  # 如果上级目录不存在则无法创建文件夹

# rmdir 删除文件夹
# FileNotFoundError: [Errno 2] No such file or directory: 'aaa/bbb'
# 如果删除的文件已经不存在,则会报错
# os.rmdir('student')
# os.rmdir('文件/students')
# 如果文件夹非空使用rmdir能否删除
# OSError: [Errno 66] Directory not empty: '文件'
# 如果文件非空则不能使用rmdir删除,需要进行递归删除
# os.rmdir('文件')


# getcwd 可以获取当前活动的工作目录 >> 类似于linux中的pwd
# C:\code\PYStudying\day08
# 默认工作目录就是我们工程所在的根目录
print(os.getcwd())


# chdir  切换工作目录  >> 类似于linux中的cd
# os.chdir('文件夹')
# C:\code\PYStudying\day08\文件夹
print(os.getcwd())

# listdir  指定目录下的目录结构  >>> 类似于linux命令中的ls
# ['.idea', '01文件读写操作体验.py', '02文件的读取.py', '03文件的写入.py', '04文件的追加.py', '05文件备份案例.py', '06rename和remove.py', '07文件夹的操作.py', 'python.txt', 'python[备份].txt', 'venv', '文件夹']
# print(os.listdir())
# os.chdir('文件')
# 如果listdir括号内没有书写对应的路径,则我们使用的路径就是工作目录,如果工作目录进行了切换则查找目录结构的位置也发生了变化
# ['abcd.txt']
# print(os.listdir())

# 查询指定位置的目录结构,可以在listdir括号内填写指定的目录,我们就会查询该目录的结构
# ['abcd.txt']
#print(os.listdir('文件'))
