t1 = ('aa', 'bb', 'cc', 'dd')

# 1.下标
print(t1[0])  #>>>aa

# 2.index()   返回数据的对应下标
print(t1.index('cc'))  #>>>2
# print(t1.index('ccc')) 会报错

# 3.count()   统计某个数据在当前元组出现的次数
print(t1.count('cc'))
print(t1.count('ccc'))

# 4.len()
print(len(t1))