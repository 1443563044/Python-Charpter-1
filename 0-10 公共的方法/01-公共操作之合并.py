str1 = 'aa'
str2 = 'bb'
#字符串

list1 = [1, 2]
list2 = [10, 20]
#列表

t1 = (1, 2)
t2 = (10, 20)
#元组

dict1 = {'name': 'Tom'}
dict2 = {'age': '20'}
#字典


# 1.合并之 +
print(str1 + str2)  # >>>aabb
print(list1 + list2)  # >>>[1, 2, 10, 20]
print(t1 + t2)  # >>>(1, 2, 10, 20)
# print(dict1 + dict2)  # 字典不能合并，会报错

#加号是合并：支持字符串，列表，元组，但不支持字典
