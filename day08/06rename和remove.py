# 如果想要使用os模块中的函数，需要先导入

import os
# rename 重命名   类似于Linux中的mv命令
# 格式：os.rename(路径，新名字)
# os.rename("test.txt", "test1.txt")
# 文件可以通过rename进行移动，只需要将路径改为新的路径即可
# os.rename("test1.txt", "文件夹/test1.txt")


# remove 删除
# 格式：os.remove(路径)
# 删除文件不会进入回收站，直接删除，慎用。也没有提示
os.remove("test[备份].txt")
# 可以删除指定路径下的文件
# 如果被删除的路径不存在,则报错  (路径可以使用绝对路径,和相对路径)
# os.remove('文件/a.txt')
# os.remove('python[备份].txt')
# PermissionError: [Errno 1] Operation not permitted: '文件'
# 使用remove不能删除文件夹
os.remove('文件')
