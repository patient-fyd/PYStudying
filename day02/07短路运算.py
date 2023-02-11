# 短路运算:
a = 1
b = 2
# 当逻辑运算的第一个表达式已经可以决定整个逻辑运算的值的时候,后边的表达式将不会被运行
print(a > b and a < b)

# 在数值型数据中,非0即真
# 在容器型数据中,非空即真
# None 代表False
print(False and 1)  # False
print(0 and True)  # 0
print(12 or False)  # 12
print(None and True)  # None

print(True and False)  # False
print(True and 15)  # 15

print(False or "")  # ""

print(3 and 4 and 5)

print(True and '123')

print(5 and 6 or 7)


