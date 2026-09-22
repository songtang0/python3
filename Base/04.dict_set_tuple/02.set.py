# 集合 set ---> 无序, 不可重复, 可修改
# 定义
s1 = {5, 3, 2, 0, 9 ,12, 43, 64, 22, 5, 78}

# 定义空集合
s20 = set()
print(s20)
print(type(s20))

# 常见方法 :
# add() : 添加元素到集合
s1.add(99)
print(s1)

# remove() : 移除集合中的指定元素(指定元素不存在将报错)
s1.remove(12)
print(s1)

# pop() : 随机删除集合中的元素并返回
s3 = s1.pop()
print(f"s3:{s3}")
print(s1)

# clear() : 清空集合
s1.clear()
print(s1)

s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}
# difference() : 求两个集合的差集 (存在于第一个集合, 但不存在于第二个集合)
print(s2.difference(s3))
print(s3.difference(s2))

# union() : 求两个集合的并集
print(s2.union(s3))

# intersection() : 求两个集合的交集
print(s2.intersection(s3))
