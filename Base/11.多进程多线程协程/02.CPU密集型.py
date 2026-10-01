# CPU密集型任务，更适合用多进程。

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cpu_task(n):
    print(f'任务{n}开始了')
    total = 0
    for i in range(10000000):
        total += i * i
    return total

if __name__ == '__main__':
    print('===== 多进程完成【CPU密集型任务】=====')
    start = time.time()
    #开启四个进程进行计算
    with ProcessPoolExecutor(4) as executor:
        results = list(executor.map(cpu_task, range(1, 5)))
    end = time.time() - start
    print(f'多进程总耗时：{end}秒, 结果是:{results}')

    # print('===== 多线程完成【CPU密集型任务】=====')
    # start = time.time()
    # with ThreadPoolExecutor(4) as executor:
    #     results = list(executor.map(cpu_task, range(1, 5)))
    # end = time.time()
    # print(f'多进程总耗时：{end}秒')
