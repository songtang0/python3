import random
computerRandom = random.randint(0, 2)
print('电脑生成的随机数是: ', computerRandom)
playerGuess = int(input('请输入  (0)剪刀  (1)石头  (2) 布：'))
print('用户输入的随机数是: ', playerGuess)
if (playerGuess == 0 and computerRandom == 2) or (playerGuess == 1 and computerRandom == 0) or (playerGuess == 2 and computerRandom == 1):
    print('你赢了！')
elif playerGuess == computerRandom:
    print('平局！')
else:
    print('输了')
