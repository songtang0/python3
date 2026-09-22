import random
ran = random.randint(1, 10)
print(ran)

# for else 在for循环执行完或者没有循环数据的时候执行

name = '宋唐'
num = int(input('请输入需要的AK数量:'))
for i in range(num):
    print('{}很厉害，正在打第{}个AK'.format(name, i + 1))
else:
    print('AK没子弹了,{}没有枪了'.format(name))
