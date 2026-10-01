import os, time
from concurrent.futures import ProcessPoolExecutor

# 5️. 使用 map 方法批量提交任务
#    注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，
#    并且得到结果的顺序与任务分配的顺序是一致的。

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
    # 创建一个进程池执行器
    executor = ProcessPoolExecutor(max_workers=3)
    # 通过 map 方法批量提交任务（结果按照提交的顺序来）
    results = executor.map(work, range(1, 8))
    # 获取 results 生成器中的内容（这里会阻塞直到所有结果就绪）
    # print(list(results))
    print(results)
    # 等所有任务都完成
    executor.shutdown(wait=True)
    print('---------end-------------')
