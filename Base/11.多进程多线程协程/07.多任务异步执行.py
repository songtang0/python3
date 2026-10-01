import asyncio, time

async def work(n, delay):
    print(f'work{n}开始')
    print(f'work{n}执行中......')
    await asyncio.sleep(delay)
    print(f'work{n}结束')
    return f'work{n}的返回值'

async def main():
    print('main开始')
    start = time.time()
    # task1 = asyncio.create_task(work(1, 5))
    task1 = asyncio.create_task(work(1, 2))
    task2 = asyncio.create_task(work(2, 2))
    task3 = asyncio.create_task(work(3, 2))

    # 此处会等待task1执行完成
    res1 = await task1
    print(res1)

    #等待上面的task1完成后，再等待task2完成
    res2 = await task2
    print(res2)

    #等待上面的task2完成后，再等待task3完成
    res3 = await task3
    print(res3)
    print('main结束', time.time() - start)
    return '我是main的返回值'

result = asyncio.run(main())
print(result)
