'''
步骤：
  1.导入模块
    import random
  2.使用模块的功能
    random.randint(开始,结束)
'''

import random

# 1. 出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))

# 电脑
computer = random.randint(0, 2)

# 1.5 用实际文字表达出双方出的是什么
shiji = player
if player == 1:
    shiji = "剪刀"
elif player == 0:
    shiji = "石头"
elif player == 2:
    shiji = "布"
else:
    print('请根据提示输入相对应的数字')

shiji1 = computer
if computer == 1:
    shiji1 = "剪刀"
elif computer == 0:
    shiji1 = "石头"
elif computer == 2:
    shiji1 = "布"
print(f'你出的是{shiji}，电脑出的是{shiji1}.')

# 2.判断输赢
# 玩家胜利：
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('恭喜你，你赢了')
#平局
elif player == computer :
    print('平局，再来一次')
#电脑获胜（最后一种情况，直接用else，而不是elif）
else:
    print('很遗憾，你输了')
