# 字典 -- key不能重复(如果重复, 后面的值, 会覆盖前面的值)、key必须得是不可变类型（str，int，float，tuple）

dict1 = {"chen":670, "程咬金":608, "鲁班七号":580, "貂蝉":688}
print(dict1)
print(type(dict1))

# key必须得是不可变类型（str，int，float，tuple）, 不能是 list、set、dict
dict2 = {0: 567, 1.6: 4567, (1, 2): 987, ('A', 'B'): 'jack'}
print(dict2)

# 访问
print(dict1['chen'])
dict1['chen'] = 666 # 修改 - key存在就是修改
print(dict1['chen'])

print(dict1.get('chen'))

print(dict1.keys()) # 获取所有的key
print(f'就莱克斯顿非：{dict1.values()}') # 获取所有的value
print(dict1.items()) # 获取所有的键值对 key:value

# ---------------------------------------- 字典 常见操作 ---------------------------------------
# 添加 - key不存在就是添加
dict1['刘备'] = 999

# 删除
del dict1['chen']
print(dict1)

# 遍历
for key in dict1.keys():
    print(f'{key}: {dict1[key]}')
for value in dict1.items():
    print(f'items: {value}-{value[0]}: {value[1]}')
for k,v in dict1.items():
    print(f'KV: {k}: {v}')