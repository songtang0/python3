# 案例3: 生成1-20的平方列表。 --> range(1,21)

# 方式一: 传统方式
num_list = []
for i in range(1, 21):
    num_list.append(i**2)
print(num_list)

# 方式二: 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式1: [要插入的值 for i in 序列/列表]
num_list2 = [i**2 for i in range(1, 21)]
print(num_list2)

# 案例4: 从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表。 ---> 判断偶数: num % 2 == 0
# 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式2: [要插入的值 for i in 序列/列表 if 条件]
num_list3 = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i**2 for i in num_list3 if i % 2 == 0]
print(new_list)
print(num_list3)


