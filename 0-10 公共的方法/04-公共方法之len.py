''''
len是length长度的缩写，返回的值是数据的长度

len() 计算容器中元素的个数

容器概念：容器就是变量的一个类型，就是字符串，列表，元组，字典等，容器可以装很多数据

'''

str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]
t1 = (100, 200, 300, 400, 500)
dict1 = {'name':'Tom', 'age': 20, "gender": 'Male'}

# 1.判断长度
print(len(str1))  # >>> 7
print(len(list1))  # >>> 5
print(len(t1))   # >>> 5
print(len(dict1))  # >>> 3