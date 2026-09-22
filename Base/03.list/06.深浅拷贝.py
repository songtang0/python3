from copy import copy, deepcopy

# 直接赋值：两个变量指向同一个对象，修改其中一个，就会影响另一个（互相影响）。
nums1 = [10, 20, 30, 40]
nums2 = nums1
nums2[3] = 99

# 浅拷贝：创建一个新的外层容器，但内部元素仍然引用原来的对象
clone_nums1 = [10, 20, 30, 40]
clone_nums2 = copy(clone_nums1)
clone_nums1[3] = 99
print(clone_nums1)
print(clone_nums2)

# 浅拷贝存在的问题：嵌套数据仍然是共享的，修改嵌套数据会互相影响
clone_nums3 = [10, 20, 30, [40, 50]]
clone_nums4 = copy(clone_nums3)
clone_nums3[3][0] = 99
print(clone_nums3)
print(clone_nums4)

# 深拷贝：创建一个新的外层容器，并对其内部所有的【可变子对象】进行递归复制
# 备注：
#   1.深拷贝可以彻底消除数据之间的相互影响。
#   2.深拷贝遇到【不可变对象】不会复制，会直接引用。
deep_clone_nums1 = [10, 20, 30, [40, 50]]
deep_clone_nums2 = deepcopy(deep_clone_nums1)
deep_clone_nums2[3][0] = 99
print(deep_clone_nums1)
print(deep_clone_nums2)

# 注意点：
#   1.深拷贝只复制可变对象，不可变对象会直接引用。
a = 666
b = deepcopy(a)
print(id(a))
print(id(b))

#   2.元组中如果只包含不可变对象，则深拷贝没有效果。
tuple_nums1 = (10, 20, 30, [40, 50])
tuple_nums2 = deepcopy(tuple_nums1)
print(id(tuple_nums1))
print(id(tuple_nums2))
