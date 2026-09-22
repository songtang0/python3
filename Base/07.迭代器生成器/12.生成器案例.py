# 用生成器实现遍历Person类的实例对象
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__attrs = [name, age, gender, address]
    def __iter__(self):
        # yield self.name
        # yield self.age
        # yield self.gender
        # yield self.address
        yield from self.__attrs
p = Person('鲁班七号', 28, '男', '王者峡谷')
print(p)
# 目标：
for attr in p:
    print(attr)

# 用生成器实现斐波那契数列
def fiboo(total):
    pre = 1
    cur = 1
    for index in range(total):
        if index < 2:
            yield 1
        else:
            value = pre + cur
            pre, cur = cur, value
            yield value
f1 = fiboo(10)
print(f1)
# for item in f1:
#     print(item)
# 无论是迭代器，还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容（注意：容易挤爆内存）
print(list(f1))

# 生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方式。
# 语法格式：(表达式 for 变量 in 可迭代对象)
# 什么时候适合用生成器表达式？———— 当"每个结果，只依赖当前这一个元素"时。
nums = [10, 20, 30, 40]
# 列表推导式
res1 = [n * 2 for n in nums]
print(res1)

res2 = (n * 2 for n in nums)
print(res2)
for item in res2:
    print(item)
