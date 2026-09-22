n = 1
while n <= 5:
    m = 1
    while m <= n:
        print('*', end='')
        m += 1
    print()
    n += 1
s1 = 72
s2 = 85
# r = (85-72)/72
# print(r)
# print("小明的成绩提升了：{0:0.1%}".format(r))
r = (s2-s1)/s1*100
print('%.1f%%' % r)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
