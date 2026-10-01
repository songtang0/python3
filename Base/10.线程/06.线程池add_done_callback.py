import os, time
from concurrent.futures import ThreadPoolExecutor
from threading import get_native_id, RLock

# 4️⃣使用 add_done_callback 方法，为任务添加完成时的回调函数
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
    # 创建一个线程池执行器
    executor = ThreadPoolExecutor(3)
    lock = RLock()
    # 收集每个线程的执行结果
    result_list = []
    def done_func(f):
        result_list.append(f.result())
    # 使用submit提交任务，并指定回调函数
    for index in range(1, 8):
        f = executor.submit(work, index, lock)
        f.add_done_callback(done_func)
    # 阻塞主线程，等待线程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    # 打印最终的结果
    print(result_list)
    print('---------end-------------')


