# 报数，如果尾数是7，或者是7的倍数，则跳过
# 报数结束，显示有多少人报数

count = 0

for i in range(1,51):
    if i % 10 == 7 or i % 7 == 0:
        continue
    count += 1
    print(i)
else:
    print(f'一共有{count}人报数')