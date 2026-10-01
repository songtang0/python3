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
    result = await asyncio.gather(work(1, 2), work(2, 2), work(3, 2))
    print(result)
    print('main结束', time.time() - start)
    return '我是main的返回值'

result = asyncio.run(main())
print(result)
