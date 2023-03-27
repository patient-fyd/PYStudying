# add 增加
set1 = {1, 2, 3, 4}
# set 在使用add命令后,不会产生新的数据,而是原集合中进行修改
set1.add(5)
print(set1)  # {1, 2, 3, 4, 5}

# update 更新
# TypeError: 'int' object is not iterable
# update内部只能填写容器类型(数据序列)
# set1.update(6)
set1.update([6, 7])
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
# 如果更新的数据已经存在,则去重
set1.update([1,2])
print(set1)  # {1, 2, 3, 4, 5, 6, 7}


# remove
set1 = {1, 2, 3, 4}
# 使用remove可以删除指定值的元素
# set1.remove(3)
# print(set1)  # {1, 2, 4}

# pop 随机删除一个元素,并且将删除的元素返回
# print(set1.pop())
# print(set1)

# discard
# 如果使用remove删除的元素不存在会怎样?  报错
# set1.remove(13)  # KeyError: 13
# 如果使用discard删除元素呢?  不会报错
set1.discard(3)
print(set1)  # {1, 2, 4}
set1.discard(13)
print(set1)


# 数据是否在集合中
set1 = {1, 2, 3, 4}
# in 判断元素是否在集合中出现
print(4 in set1)  # True
print(5 in set1)  # Fasle

# not in 判断元素是否不在集合中
print(4 not in set1)  # False
print(5 not in set1)  # True

# 注意:格式  元素 in  集合

# 判断的数据必须要在集合中能够被储存
# TypeError: unhashable type: 'list'
# print([1, 2] in set1)


# for 遍历
set1 = {1, 2, 3, 4}
for i in set1:
    print(i)

# 注意遍历集合,顺序不定
name_set = {'Tom', 'Bob', 'Rose'}
for i in name_set:
    print(i)
'''
Rose
Tom
Bob
'''