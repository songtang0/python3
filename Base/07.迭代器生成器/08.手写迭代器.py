# 迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）。
# region
names = ['张三', '李四', '王五']
it1 = iter(names)
it2 = iter(names)

print(it1)
print(it2)
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))

for item in it1:
    print(f'item: {item}')

for item in it2:
    print(f'item: {item}')
# endregion

# 需求：让for循环可以遍历Person的实例对象
# 实现方式1️.
# region
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        return PersonIterator(self)
class PersonIterator:
    def __init__(self, person):
        # 将外部传进来的数据保存好
        self.person = person
        # 设置迭代器的初始化状态（指针位置）
        self.index = 0
        # 配置好要遍历的内容 存的是value，而不是key
        # self.attr = [person.name, person.age, person.gender, person.address]
        self.attr = list(vars(person).values()) # 和上面是一样的
    # 迭代器的__iter__方法会返回迭代器自身
    def __iter__(self):
        return self
    # 每次调用__next__方法，会根据当前的状态，返回下一个元素
    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.index >= len(self.attr):
            raise StopIteration
        # 获取要返回的内容
        value = self.attr[self.index]
        # 更新迭代器状态（指针位置）
        self.index += 1
        return value
# 目标：
p1 = Person('安其拉', 18, '女', '王者大峡谷')
it_p = iter(p1)
it_p2 = iter(p1)
for item in it_p:
    print(f'手写迭代器:{item}')
for item in it_p2:
    print(f'手写迭代器2:{item}')
