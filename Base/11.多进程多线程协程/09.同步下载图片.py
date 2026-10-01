import requests


def download_picture(url, filename):
    print(f'开始下载：{url}')
    response = requests.get(url)
    print('下载完毕')
    with open(filename, 'wb') as file:
        file.write(response.content)

def main():
    url_list = [
        'https://picsum.photos/id/237/800/600.jpg',
        'https://picsum.photos/id/1025/800/600.jpg',
        'https://picsum.photos/id/1069/800/600.jpg'
    ]

    for index, url in enumerate(url_list, start=1):
        download_picture(url, f'image_{index}.jpg')


main()