# CPU 密集型任务：把一个大任务拆给 4 个进程

import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def cpu_task(start, end, task_id):
    print(f'任务{task_id}开始：计算 {start} ~ {end - 1}')
    total = 0
    for i in range(start, end):
        total += i * i
    print(f'任务{task_id}完成')
    return total
def run_task(task):
    return cpu_task(*task)
if __name__ == '__main__':
    print('===== 多进程完成【CPU密集型任务】=====')
    start_time = time.time()
    # 总计算范围
    total_count = 100_000_000

    # 拆成 4 份
    chunk_size = total_count // 4

    tasks = [
        (0, chunk_size, 1),
        (chunk_size, chunk_size * 2, 2),
        (chunk_size * 2, chunk_size * 3, 3),
        (chunk_size * 3, total_count, 4)
    ]

    # 开启 4 个进程
    with ProcessPoolExecutor(4) as executor: # 0.8298125267028809 秒
    # with ThreadPoolExecutor(4) as executor: # 2.7150728702545166 秒

        # 把 4 个任务分别交给 4 个进程
        results = list(
            executor.map(
                run_task,
                tasks
            )
        )

    # 把 4 个进程的结果合并
    total = sum(results)
    end_time = time.time() - start_time

    print(f'4个子任务的结果：{results}')
    print(f'最终结果：{total}')
    print(f'多进程总耗时：{end_time} 秒')