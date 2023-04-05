# 需求：用户输入一个文件名，通过为你教案读写操作进行文件备份，备份文件名为原文件名加上备份后缀
# 例如：输入test.txt，备份文件名为test[备份].txt

# 1.获取用户输入的文件名
old_file_name = input('请输入要备份的文件名：')
file = open(old_file_name, 'r', encoding='utf-8')

# 2.构造备份文件名,拼接备份文件名
copy_file_name = old_file_name.replace('.', '[备份].')
# 打开新文件
copy_file = open(copy_file_name, 'a', encoding='utf-8')
# # 读取旧文件内容
# content = file.read()
# # 写入新文件
# copy_file.write(content)
# 一般情况下，文件都是指定单次读取最大字符的
while True:
    content = file.read(3)
    if len(content) == 0:
        break
    copy_file.write(content)

# 3.关闭文件
file.close()
copy_file.close()


