
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置迭代器的初始化状态（指针位置）
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]
    def __iter__(self):
        self.__index = 0
        return self
    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.__index >= len(self.__attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attrs[self.__index]
        # 更新迭代器状态（指针位置）
        self.__index += 1
        # 返回value
        return value

# 目标：
# 下面的p1既是可迭代对象，又是迭代器
p1 = Person('张三', 18, '男', '北京昌平')
# print(p1)
# print(p1.__dict__)
for item in p1:
    print(item)

for item in p1:
    print(item)
