import os, time
from concurrent.futures import ProcessPoolExecutor
# 4️. 使用 add_done_callback 方法，为任务添加完成时的回调函数
# 整理效果和 16 基本上是一样的
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
    executor = ProcessPoolExecutor(3)
    # 准备一个 result_list 列表去收集任务的结果
    result_list = []
    # 任务完成后的回调函数
    def done_func(future):
        result_list.append(future.result())
    # 开启7个任务，并指定回调函数
    for i in range(1, 8):
        f = executor.submit(work, i)
        f.add_done_callback(done_func)
    # 等所有任务都完成
    executor.shutdown(wait=True)
    # 打印最终的结果（按"完成的顺序"获取）
    print(result_list)
    print('---------end-------------')

