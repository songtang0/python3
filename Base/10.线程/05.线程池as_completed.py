import os, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import RLock

# 3️. 使用 as_completed：按"完成顺序"获取结果
def work(n, lock):
    with lock:
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
    executor = ThreadPoolExecutor(3)
    lock = RLock()
    # 使用 submit 方法提交任务（submit 只负责"提交任务"，不会阻塞主进程）
    futures = [executor.submit(work, index, lock) for index in range(1, 8)]
    # 准备一个 result_list 去收集任务的具体结果
    result_list = []
    # 收集每个任务的结果（按完成顺序）
    for f in as_completed(futures):
        result = f.result()
        # 主线程打印时也使用同一把锁
        with lock:
            print(f'嘿嘿，{result}', flush=True)
        # result_list 只由主线程修改，不需要加锁
        result_list.append(result)
    # 阻塞主进程，等待进程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    # 打印最终结果
    print(result_list)
    print('---------end-------------')

