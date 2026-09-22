# 千峰29
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

# pass 关键字在Python里没有意义，只是单纯的用来占位，保证语句的完整性
height = 1.79
weight = 106
desc = '大于100' if weight > 100 else '小于100'
bmi = weight / height**2
description = ''
print(bmi)
if bmi < 18.5:
    description = '过轻'
elif 18.5 <= bmi < 25: 
    description = '正常'
elif 25 <= bmi < 28:
    description = '过重'
elif 28 <= bmi < 32:
    description = '肥胖'
else:
    description = '严重肥胖'
print(description)

num1 = int(input('请输入num1:'))
num2 = int(input('请输入num2:'))
res = num1 if num1 > num2 else num2
print(res)
print(desc)
