# 元组基本操作 - tuple ---> 元素可以重复, 有序, 不可修改
# 定义
t1 = (80, 95, 78, 50, 76, 80, 85, 20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

# count() 统计元素的个数
print(t1.count(80))
# index() 获取元素的索引(第一个元素的位置)
print(t1.index(80))

# 注意点: 如果定义单元素的元组, 单个元素之后需要加上逗号, 比如 (100,)
t2 = ()
print(t2)
print(type(t2))

t3 = (100,)
print(t3)
print(type(t3))

# --------------------------------------------- 元组 tuple 组包与解包 ---------------------------------------------------
# 组包操作
t1 = (5, 7, 9, 10, 2, 23, 12)
t2 = 5, 7, 9, 10, 2, 23, 12
print(t1)
print(t2)
# 解包操作
# 基础解包(变量数量与容器的元素个数一致)
a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)

# * 扩展解包 (* 收集剩余的所有元素, 封装列表list中)
first,second, *other, last = t1
print(first,second)
print(other)
print(last)

