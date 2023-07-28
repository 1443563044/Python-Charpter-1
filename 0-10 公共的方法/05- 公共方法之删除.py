''''
语法：del 目标   或者   del(目标)

'''

str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]
t1 = (100, 200, 300, 400, 500)
dict1 = {'name':'Tom', 'age': 20, "gender": 'Male'}

#1.字符串
del(str1)
# print(str1) 程序报错，因为str1已经被删除了

# 2. 列表
del(list1[0])  #列表的下标。知识点:列表切片
print(list1)

del(list1)
# print(list1) 报错，因为被删了

# 3. 元组
del(t1) #元组不支持单个数据修改
# print(t1)  报错

# 4. 字典
del dict1['name']
print(dict1)  #删除了整个 'name' 键值对

del dict1
# print(dict1) 程序报错