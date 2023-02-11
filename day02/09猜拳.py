
import random  # 导入模块
# 玩家键入拳型
player = int(input('请输入您要出的拳型:(0 石头 1 剪刀 2 布)'))
# 电脑随机出拳
# 在计算机中如果想要生成随机数据可以使用random模块进行生成

# 生成随机数  random.randint(m,n) 生成[m, n]区间内的任意一个整数
computer = random.randint(0, 2)
result = player - computer
# 比对拳型
# 玩家获胜情况: p: 0 c: 1  |  p: 1  c: 2  | p : 2  c : 0
if result == -1 or result == 2:
    # 输出结果
    print('玩家获胜')
elif result == 0:
    # 输出结果
    print('平局')
else:
    # 输出结果
    print('电脑获胜')
