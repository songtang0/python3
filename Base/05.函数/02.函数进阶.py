# ----------------------------------------- 函数 - 变量的作用域 -----------------------------------------
# 全局变量 : 在函数外部 或 函数的内部都是可以访问的 ;

num = 100
def circle_area(r):
    # 局部变量 只能在函数内部使用
    pi = 3.14159
    area = pi * r * r
    print("num=", num)
    return area

c_area = circle_area(10)
print(c_area)
print("num=", num)

# ----------------------------------------- 函数 - 传参方式 -----------------------------------------
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}
# 传参方式一: 位置参数
print(reg_stu("宋唐", 28, "男", "北京"))

# 传参方式二: 关键字参数
print(reg_stu(city="北京", name="宋唐", age=28, gender="男"))

# 传参方式三: 位置参数 + 关键字参数 ---> 位置参数在前, 关键字参数在后
print(reg_stu("宋唐", 28, city="北京", gender="男"))

# ----------------------------------------- 函数 - 不定长参数(位置参数 *args --> 元组) -----------------------------------------
# 需求: 根据传入的这批数据, 计算这批数据的最小值, 最大值, 平均值
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)
print(calc_data(2, 7, 9, 10, 45))
print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))

# ----------------------------------------- 函数 - 不定长参数(关键字参数 **kwargs --> 字典) ----------------------------------
# 需求: 根据传入的这批数据, 计算这批数据的最小值, 最大值, 平均值
"""
根据传入的这批数据, 计算这批数据的最小值, 最大值, 平均值
:param args: 不定长位置参数, 需要计算的这批数据
:param kwargs: 不定长关键字参数
     round: 保留的小数位个数
     print: 是否打印输出
:return: 最小值, 最大值, 平均值
"""
def calc_data2(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值:{avg_data}")
    return min_data, max_data, avg_data
print(calc_data2(2, 7, 9, 10, 45, round=1, print=True))
