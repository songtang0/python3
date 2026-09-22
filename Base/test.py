def demo():
    print('demo函数开始执行了')
    print(100)
    yield '我是第1个yield所返回的数据'
    a = 200
    print(a)
    yield '我是第2个yield所返回的数据'
    b = 300
    print(b)
    return '尚硅谷'

d = demo()
# 验证：生成器对象d，和迭代器一样，也拥有：__iter__  和 __next__ 方法
print(hasattr(d, '__iter__'))
print(hasattr(d, '__next__'))

# 验证：生成器对象的__iter__方法，和迭代器一样，返回的也是自身
result = iter(d)
print(result == d)

# for循环遍历生成器
for item in d:
    print(item)