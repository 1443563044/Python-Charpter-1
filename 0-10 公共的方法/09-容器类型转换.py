list1 = [10, 10, 10, 40, 50]
t1 = (100, 300, 400, 500)
dict1 = {100, 200, 300, 400, 500} #集合

#  注意！！！
# 集合可以快速完成列表去重
# 集合不支持下标


# 1.list()  将某一个序列转换成列表
print(list(t1))
print(list(dict1))

# 2.set()  将某一个序列转换成集合
print(set(list1))
print(set(t1))


# 3.tuple() 将某一个序列转换元组
print(tuple(list1))
print(tuple(dict1))


