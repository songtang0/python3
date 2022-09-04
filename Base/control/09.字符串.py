nameStr = '刘备 关羽 张飞 赵云 诸葛亮'
nameList = nameStr.split(' ')
nameListR = nameStr.rsplit(' ', 1)
print(nameList)
print(nameListR)

print('-'*20)
nameModule = """若有人兮山之额
披薜荔兮带女萝
既含睇兮又宜笑
子慕予兮善窈窕
"""
print(nameModule.splitlines())

print('空格处理' + '-'*50)
# 空格
empty = ' admin     '
print(len(empty))
print(len(empty.strip())) # 去掉左右两侧的空格部分
