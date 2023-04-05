# write 写入
# 当文件读写模式时，'w'可以使用write方法写入内容

# 如果文件不存在，会自动创建文件
# file = open('test.txt', 'w', encoding='utf-8')
# 当文件执行写入操作时，会将原有内容清空
file = open('python.txt', 'w', encoding='utf-8')

print(file)

# file.write('hello world')
# # 写入会写入格式化字符串
# file.write("""
# hello world
# hello world""")


# file.writelines(['hello world', 'hello world'])
# writelines 传入一个列表,列表中的每个元素都会写入到文件中
lines = ['hello world\n', 'hello world\n', 'hello world hello world']
file.writelines(lines)

file.close()