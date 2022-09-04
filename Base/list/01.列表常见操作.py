baseList = ['宋唐', '楚厦', 'Song']
secondList = [3, 25]
baseList.insert(1, '厉害')
print(baseList)
baseList.extend(secondList)
print(baseList)

del secondList
# print(secondList)
baseList.pop()
print(baseList)
baseList.remove('Song')
print(baseList)
