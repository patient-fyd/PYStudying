# 'a'模式写入: 会在文件末尾追加内容

file = open('python.txt', 'a', encoding='utf-8')

# 在追加模式下打开文件，如果文件不存在，会自动创建文件
file = open('test.txt', 'a', encoding='utf-8')

# 进行追加操作
# file.write('hello world')
file.write('   python')


file.close()
