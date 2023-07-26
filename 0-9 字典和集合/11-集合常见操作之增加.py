''''
增加有两种：
1.add()
只能添加一个数据，如果添加两个会报错
集合数据是没有顺序的，所以添加进去的时候是随机的

2.update()

'''


s1 = {10, 20}

# 1. add()
s1.add(100)
print(s1)

s1.add(100)
print(s1)

#第二次添加不会发生任何事
# s1.add(100, 'Tom')  报错
# s1.add([100, 200, 300]) 报错

# 2.update() 增加的数据是序列
s2 = {10, 20}
s2.update([10, 20, 30, 40, 50])
print(s2)
#集合有去重功能，增加了重复数据是会自动去重


s2.update('abc')
print(s2)
#拆分abc并追加到s2中

'''

s2.update(100)
返回：TypeError: 'int' object is not iterable
100是int数据类型，不支持迭代，即100拆不开，像tom，可以拆成't' , 'o' , 'm'
注意！  s2.update(100) 增加单一数据时程序会报错

'''