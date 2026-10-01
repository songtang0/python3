import os, time
from concurrent.futures import ThreadPoolExecutor
from threading import RLock, get_native_id

# 2️. 获取子线程执行后的返回结果（Future类的实例对象 + result方法）
def work(n, lock):
    with lock:
        print(f'work正在执行任务{n}.........{get_native_id()}')
    time.sleep(1)
    return f'任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    # 创建一个线程池执行器
    executor = ThreadPoolExecutor(max_workers=3)
    lock = RLock()
    # 使用 submit 方法提交任务（submit 只负责”提交任务”，不会阻塞主线程）
    futures = [executor.submit(work, index, lock) for index in range(1, 8)]
    # 阻塞主线程，等待线程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    # 打印结果
    for f in futures:
        print(f.result())
    print('---------end-------------')
