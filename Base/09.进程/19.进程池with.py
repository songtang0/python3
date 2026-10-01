# 6️. 使用 with：进程池的"自动回收"写法
#    离开 with 代码块时自动执行 shutdown(wait=True)

import os, time
from concurrent.futures import ProcessPoolExecutor

def work(n):
    print(f'work正在执行任务{n}.........{os.getpid()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'我是任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    # with 语句自动管理进程池生命周期，退出时自动 shutdown
    with ProcessPoolExecutor(max_workers=3) as executor:
        # 通过 map 方法批量提交任务（结果按照提交的顺序来）
        results = executor.map(work, range(1, 8))
        # 获取 results 生成器中的内容
        print(list(results))
    print('---------end-------------')
