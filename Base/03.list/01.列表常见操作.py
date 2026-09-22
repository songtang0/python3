baseList = ['宋唐', '楚厦', 'Song']
secondList = [3, 25]
baseList.append('GPT')
baseList.insert(1, '厉害')
print(baseList)
baseList.extend(secondList)
print(baseList)

del secondList
# print(secondList)
baseList.pop()
print(baseList)
baseList.remove('Song')
print(baseList)

# 定义列表 - list
s = [56, 90, 88, 65, 90, "A", "Hello", True]

print(type(s)) # <class 'list'>

# 访问列表元素
# 获取
print(s[0]) # 正向索引, 从0开始
print(s[-1]) # 反向索引, 从-1开始

# 修改
s[5] = "加油"
print(s)

# 注意: 如果指定的索引, 超出范围, 将会报错 list assignment index out of range
# s[10] = "DEF"
# print(s)

# 删除
del s[2]
print(s)

# 遍历
for item in s:
    print(item)
