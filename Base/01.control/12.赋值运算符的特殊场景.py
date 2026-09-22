# 等号连接的变量可以传递赋值
a = b = c = d = 'song'
print(a, b, c, d)

m, n = 3, 5  # 拆包
print(m, n)

x = 'hello', 'good', 'yes'
print(x)

y, *z, p = 1, 2, 3, 4, 5, 6  # * 表示可变长度
print(y, z, p)
