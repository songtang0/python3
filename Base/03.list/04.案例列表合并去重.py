# 案例2: 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 解包: 将列表这一类容器解开成一个一个独立的元素
# 组包: 将多个值合并到一个容器
num_list = [*num_list1, *num_list2] # num_list1 + num_list2也可以
print("合并后的原始列表: ", num_list)

new_list = [] # 去重重复记录后的列表
for num in num_list:
    # 判断new_list中是否存在num元素, 如果不存在, 再添加
    if num not in new_list:
        new_list.append(num)
print("去重重复记录后的列表: ", new_list)


