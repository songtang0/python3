strA = 'SongTang_1'
strB = 'song tang_1'
strC = '  Song tang      '
strAFind = strA.find('_')
strAIndex = strA.index('Tang')
print(strAFind)
print(strAIndex)
print(strA[strA.rfind('_'):])
print(strA.startswith('Song'))
print(strA.endswith('1'))
print(strA.isalpha())  # 纯字母组成
print(strA.isdigit())  # 数字组成
print(strA.isalnum())  # 数字或者字母
print(strA.isspace())  # 是否是空格
print(' '.isspace())  # 是否是空格
print('SONG'.isupper())  # 大写
print('SONG'.islower())  # 小 写
print(strA.count('1', 3, len(strA) - 1))
print('capitalize：', strB.capitalize())  # 第一个单词的首字母大写
print('title: ', strB.title())  # 每个单词的首字母大写
print('lower', strB.lower())  # 所有都变成小写
print('upper', strB.upper())  # 所有都变成大写

print('空格处理：----------------------')

print(strB.ljust(20), len(strB.ljust(20)))  # 返回指定长度的字符串，并在右侧使用空白字符补全(左对齐)。
print(strB.rjust(20), len(strB.rjust(20)))  # 返回指定长度的字符串，并在左侧使用空白字符补全(右对齐)。
print('center:', strB.center(10))  # 返回指定长度的字符串，并在两端使用空白字符补全(居中对齐)
print('lstrip: ', strC.lstrip(), len(strC.lstrip()))  # 删除左边的空白字符
print('rstrip: ', strC.rstrip(), len(strC.rstrip()))  # 删除右边的空白字符
print('strip: ', strC.strip(), len(strC.strip()))  # 删除两断的空白字符
