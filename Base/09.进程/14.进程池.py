import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# 1️. 创建『进程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
def work(n):
    print(f'work正在执行任务{n}.........{os.getpid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('---------start-------------')
    # 创建一个进程池执行器
    executor = ProcessPoolExecutor(3)
    # 使用 submit 方法提交任务（submit 只负责"提交任务"，不会阻塞主进程）
    executor.submit(work, 1)
    executor.submit(work, 2)
    executor.submit(work, 3)
    executor.submit(work, 4)
    executor.submit(work, 5)
    executor.submit(work, 6)
    executor.submit(work, 7)
    # shutdown 的作用：不再接收新的任务。
    # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    print('---------end-------------')
