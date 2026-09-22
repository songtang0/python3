# 1.迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
# 2.当数据量很大，不确定要用多少结果时，推荐使用迭代器。

import tracemalloc

# 使用迭代器实现
class Fibo:
    def __init__(self, total):
        self.total = total
        # 当前生成到第几个了（计数器，指针）
        self.index = 0
        # 初始的两个值
        self.pre = 1
        self.cur = 1
    def __iter__(self):
        return self
    def __next__(self):
        # 当生成足够数量后，抛出StopIteration异常
        if self.index >= self.total:
            raise StopIteration
        if self.index < 2:
            value = 1
        else:
            value = self.pre + self.cur
            self.pre = self.cur
            self.cur = value
        self.index += 1
        return value

# 不用迭代器实现
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for i in range(2, total):
        nums.append(nums[i-1] + nums[i-2])
    return nums
# 看内存占用
tracemalloc.start()
f1 = Fibo(100000)
m = tracemalloc.get_traced_memory()[1]
print(f'内存占用是：{m / 1024 / 1024}MB') # 内存占用是：0.00031280517578125MB

tracemalloc.start()
f2 = fibo(100000)
# print(f2)
m = tracemalloc.get_traced_memory()[1]
print(f'内存占用是：{m / 1024 / 1024}MB') # 内存占用是：444.9928092956543MB

# 迭代器适合按需生成、流式处理或只使用部分结果；如果最终必须保存全部结果，迭代器通常不能消除保存这些结果所需要的内存。
f1 = Fibo(100000)
for n in f1:
    if n > 100:
        break
    print(n)
