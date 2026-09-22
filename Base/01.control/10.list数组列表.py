newList = ['牛奶']
secondList = [0, 1]
print(newList)
newList.append('面板')
print(newList)
print(newList + secondList)
secondList.extend([3])
print(secondList)

target = ['面包', 1, 2, 6, '酸奶', '酸奶', '牛肉']
copyTarget = target[0:]
for i in copyTarget:
    if i == '酸奶':
        target.remove(i)
print(target, copyTarget)
