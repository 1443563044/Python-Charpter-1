name_list = ['Boer', 'Tony', 'Lily']

# 1.添加一个字符串数据
name_list.append('Tom')
print(name_list)


# 2. 添加一个列表数据,追加整个序列到列表结尾
name_list.append([1,2,3,44])
name_list.append(['Xiaoming' , 'xiaohong'])  #添加列表内的字符串时要用 'xxx'
print(name_list)
print(type(name_list[5]))
#列表数据是可以改变的 -- 列表是可变数据类型