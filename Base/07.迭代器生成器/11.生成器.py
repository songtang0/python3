# 1️. 生成器：
#   1.生成器函数：函数体中如果出现了 yield 关键字，那该函数是『生成器函数』。
#   2.生成器对象：调用『生成器函数』时，其函数体不会立刻执行，而是返回一个『生成器对象』。
#   备注：不管能否执行到 yield 所在的位置，只要函数中有 yield 关键字，那该函数，就是『生成器函数』。

def demo():
    print('demo函数开始执行了')
    print(100)
    yield
    a = 200
    print(a)
d = demo()
print(d)

# 2️. 写在『生成器函数』中的代码，需要通过『生成器对象』来执行：
#   1.调用『生成器对象』的 __next__ 方法，会让『生成器函数』中的代码开始执行。
#   2.当『生成器函数』中的代码开始执行后，遇到 yield 会"暂停"执行，并且其内部会记录"暂停"的位置。
#   3.后续调用 __next__ 方法时，都会从上一次"暂停"的位置，继续运行，直到再次遇到 yield。
#   4.遇到 return 会抛出 StopIteration 异常，并将 return 后面的表达式，作为异常信息。
#   5.yield 后面所写的表达式，会作为本次 __next__ 方法的返回值。
def demo2():
    print('demo函数开始执行了')
    print(100)
    yield '我是第1个yield所返回的数据'
    a = 200
    print(a)
    yield '我是第2个yield所返回的数据'
    b = 300
    print(b)
    return '尚硅谷'

print('------d2 start------')
d2 = demo2()
print(next(d2))
print(next(d2))
try:
    next(d2)
except StopIteration as e:
    print(e)
print('------d2 end------', end="\n\n")

# 3️.生成器对象是一种特殊的迭代器（本质是通过 yield 自动实现了迭代器协议）。
print('------d3 start------')
d3 = demo2()
# 验证：生成器对象d，和迭代器一样，也拥有：__iter__  和 __next__ 方法
print(hasattr(d3, '__iter__'))
print(hasattr(d3, '__next__'))

# 验证：生成器对象的__iter__方法，和迭代器一样，返回的也是自身
print(iter(d3) == d3)

# for循环遍历生成器
# for item in d3:
#     print(item)

# for循环背后的逻辑
gen = iter(d3)
while True:
    try:
        value = next(gen)
        print(value)
    except StopIteration:
        break
print('------d3 end------', end="\n\n")

# 4️. yield 也能写在循环里
print('------d4 start------')
def create_car(total):
    for index in range(total):
        yield f'我是第{index + 1}台车'
# cars是生成器对象
cars = create_car(5)
# 调用一次cars的__next__方法，就会得到一台车
c1 = next(cars)
print(c1)
c2 = next(cars)
print(c2)
c3 = next(cars)
print(c3)
c4 = next(cars)
print(c4)
c5 = next(cars)
print(c5)

# for car in cars:
#     print(car)
print('------d4 end------', end="\n\n")

# 5️. yield from 能把一个『可迭代对象』里的东西依次 yield 出去。(替代：for + yield)
print('------d5 start------')
def demo5():
    nums = [10, 20, 30, 40]
    yield from nums
d5 = demo5()
print(d5)

r1 = next(d5)
print(r1)
r2 = next(d5)
print(r2)
r3 = next(d5)
print(r3)
r4 = next(d5)
print(r4)
# for item in d5:
#     print(item)
print('------d5 end------', end="\n\n")

# 6️. 使用：生成器.send(值) 可以让生成器继续执行的同时，给上一次 yield 传值。
# 备注1：next 只能取值，send 既能取值，也能送值
# 备注2：第一次启动生成器，不能传值！
print('------d6 start------')
def demo6():
    print('demo函数开始执行了')
    print(100)
    a = yield '我是第1个yield所返回的数据'
    print(a)
    b = yield '我是第2个yield所返回的数据'
    print(b)
    return '尚硅谷'
d6 = demo6()
r1 = d6.send(None)
print(r1)
r2 = d6.send(666)
print(r2)
try:
    d6.send(888)
except StopIteration as e:
    print(e)

print('------d6 end------', end="\n\n")

