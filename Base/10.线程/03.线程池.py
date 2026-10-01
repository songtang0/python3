import os, time
from threading import get_native_id, RLock
from concurrent.futures import ThreadPoolExecutor

# 1️. 创建『线程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
def work(n, lock):
    with lock:
        print(f'work正在执行任务{n}.........{get_native_id()}')
    time.sleep(1)

if __name__ == '__main__':
    print('---------start-------------')
    # 创建一个线程池执行器
    executor = ThreadPoolExecutor(max_workers=3)
    lock = RLock()
    # 使用 submit 方法提交任务（submit 只负责”提交任务”，不会阻塞主线程）
    executor.submit(work, 1, lock)
    executor.submit(work, 2, lock)
    executor.submit(work, 3, lock)
    executor.submit(work, 4, lock)
    executor.submit(work, 5, lock)
    executor.submit(work, 6, lock)
    executor.submit(work, 7, lock)
    # shutdown 的作用：不再接收新的任务。
    # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    print('---------end-------------')
