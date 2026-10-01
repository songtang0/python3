import asyncio
import requests
import aiohttp


async def download_picture(session, url, filename):
    print(f'开始下载：{url}')
    # 发送网络请求，获取这张图片，请求发出后，要等待服务器把数据返回，等待的这段时间就是IO等待
    response = await session.get(url)
    # 等待数据，图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是IO等待
    content = await response.read()
    print('下载完毕')
    with open(filename, 'wb') as file:
        file.write(content)
    #释放连接资源，告诉aiohttp，这个链接我不用了，你可以回收了
    await response.release()

async def main():
    url_list = [
        'https://picsum.photos/id/237/800/600.jpg',
        'https://picsum.photos/id/1025/800/600.jpg',
        'https://picsum.photos/id/1069/800/600.jpg'
    ]

    # 创建会话对象(发请求的工具)
    session = aiohttp.ClientSession()
    coroutines = [download_picture(session, url, f'image_{index}.jpg') for index, url in enumerate(url_list)]

    # 将多个协程对象交给事件循环
    await asyncio.gather(*coroutines)

    # 关闭会话
    await session.close()

asyncio.run(main())
