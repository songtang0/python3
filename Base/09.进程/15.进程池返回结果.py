# 2️. 获取子进程执行后的返回结果（Future类的实例对象 + result方法）
import os, time
from concurrent.futures import ProcessPoolExecutor


def work(n):
    print(f'work正在执行任务{n}.........{os.getpid()}')
    time.sleep(1)
    return f'我是任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    # 创建一个进程池执行器
    executor = ProcessPoolExecutor(3)
    # 使用 submit 方法提交任务（submit 只负责"提交任务"，不会阻塞主进程）
    futures = [executor.submit(work, index) for index in range(1, 8)]
    # 阻塞主进程，等待进程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    for future in futures:
        print(future.result())
    print('---------end-------------')

