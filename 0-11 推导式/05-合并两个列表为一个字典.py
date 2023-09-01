'''
合并两个列表为字典

len()统计序列中数据的个数


'''
# 例子1：
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man' ]

dict1 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict1)


# 例子2：
list3 = ['name', 'age', 'gender', 'id']
list4 = ['Tom', 20, 'man' ]

dict2 = {list3[i]: list4[i] for i in range(len(list4))}
print(dict2)

dict3 = {list3[i]: list4[i] for i in range(len(list3))}
print(dict2)
#>>>程序报错


# 总结：
# 1.如果两个列表数据个数相同，len统计任何一个列表的长度都可以
# 2. 如果两个列表数据不同，len统计数据的多的列表数据个数会报错：len统计数据少的列表不会报错
# （分别用len(list3)，和len(list4)来写）