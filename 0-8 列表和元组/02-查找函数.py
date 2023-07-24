name_list = ['Boer', 'Tony', 'Lily']


# 1. index() 返回指定数据所在位置的下标
print(name_list.index('Tony'))
# print(name_list.index('Tonys'))
#不存在则报错：ValueError: 'Tonys' is not in list


# 2. count()  统计指定数据在当前列表中出现的次数
print(name_list.count('Tony'))  #区分大小写


# 3.len() 访问列表长度，即列表中数据的个数
print(len(name_list))  #列表有三个数据，返回数字3