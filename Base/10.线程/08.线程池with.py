# 6️. 使用 with：线程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
import os, time
from concurrent.futures import ThreadPoolExecutor
from threading import get_native_id, RLock

def work(n, lock):
    with lock:
        print(f'work正在执行任务{n}.........{get_native_id()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    with ThreadPoolExecutor(3) as executor:
        lock = RLock()
        results = executor.map(work, range(1, 8), [lock] * 7)
        # 打印最终的结果
        print(list(results))
    print('---------end-------------')
