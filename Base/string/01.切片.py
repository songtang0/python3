"""
切片: 字符串，列表
格式: 字符串变量[start: end)
"""
s = 'ABCDEFG'
print(len(s))
print(s[1:4])
print(s[0:5])
print(s[:5])
print(s[-3:])
print(s[1:-1])
print(s[:-1:2])
print(s[4:3:-1])
x = s[:]
print(s, ':', id(s))
print(x, ':', id(x))
