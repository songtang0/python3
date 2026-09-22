# print 格式化输出

age = 18
name = '宋唐'
sex = '男'
print('这个帅气的%s孩的名字叫:%s,他说他永远%s岁' % (sex, name, age))
print('这个帅气的{}孩的名字叫:{}，他说他永远{}岁'.format(sex, name, age))
print('这个帅气的{0}孩的名字叫:{1}，他说他永远{2}岁'.format(sex, name, age))

# 简单字段名的混合使用
# 混合使用数字形式和变量名形式的字段名，可以同时传递位置参数和关键字参数。
# 关键字参数必须位于位置参数之后。
# 混合使用时可以省略数字。
# 省略字段名 {} 不能和数字形式的字段名 {非负整数} 同时使用。


# 混合使用数字形式和变量名形式的字段名
# 可以同时传递位置参数和关键字参数
print('这是一个关于{0}、{1}和{girl}的故事。'.format(
    '小明', '阿飞', girl='阿香'))
"""
这是一个关于小明、阿飞和阿香的故事。
"""

# 但是关键字参数必须位于位置参数之后
# print('这是一个关于{0}、{1}和{girl}的故事。'.format(
# '小明', girl='阿香' , '阿飞'))
"""
SyntaxError: positional argument follows keyword argument
"""

# 数字也可以省略
print('这是一个关于{}、{}和{girl}的故事。'.format(
    '小明', '阿飞', girl='阿香'))

# 但是省略字段名不能和数字形式的字段名同时出现
# print('这是一个关于{}、{1}和{girl}的故事。'.format(
#     '小明', '阿飞', girl='阿香'))
"""
ValueError: cannot switch from automatic field numbering to manual field specification
"""

# 使用元组和字典传参
# str.format() 方法还可以使用 *元组 和 **字典 的形式传参，两者可以混合使用。
# 位置参数、关键字参数、*元组 和 **字典 也可以同时使用，但是要注意，位置参数要在关键字参数前面，
# *元组 要在 **字典 前面。

# 使用元组传参
infos = '刘备', 25, '诸葛亮'
print('我是{},我今年{}'.format(*infos))
print('我是{2},我今年{1}'.format(*infos))

# 使用字典传参
venom = {'name': '小乔', 'age': 18}
print('我是{name},我现在{age}岁了'.format(**venom))

# 同时使用元组和字典传参
threeKing = '魏国', '蜀国', '吴国'
kings = {'type': '皇帝', 'name': '三国'}
print('这是{}, 我是{name}的{type}'.format(*threeKing, **kings))
print('这是{name}, 我是{1}的{type}'.format(*threeKing, **kings))

# 同时使用位置参数、元组、关键字参数、字典传参
# 注意：
# 位置参数要在关键字参数前面
# *元组要在**字典前面
tup = '鹰眼',
dic = {'weapon': '箭'}
text = '我是{1}，我怕{weakness}。我是{0}，我用{weapon}。'
text = text.format(
    *tup, '黑寡妇', weakness='男人', **dic)
print(text)
"""
我是黑寡妇，我怕男人。我是鹰眼，我用箭。
"""
