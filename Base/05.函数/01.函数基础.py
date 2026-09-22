# 函数的参数与返回值
# 函数1: 计算圆的面积 -- 半径

def circle_area(r):
    area = 3.14 * r ** 2
    return area
area1 = circle_area(100)
print(area1)

"""
根据长方形的长度和宽度, 计算长方形的面积
:param l: 长度
:param w: 宽度
:return: 长方形的面积
"""
def rectangle_area(l, w):
    area = l * w
    return area

print(rectangle_area(20, 10))

# 函数3: 计算圆的面积, 周长 -- 半径 ----> 如果返回值有多个, 多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    """
    根据圆的半径, 计算圆的面积和周长
    :param r: 半径
    :return: 圆的面积, 圆的周长
    """
    return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)
a1 = circle_area_len(10)
print(a1)
print(type(a1))

area3, len3 = circle_area_len(10)
print(area3, len3)
