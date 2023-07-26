'''
for in 循环内可写入两个随机变量，
xx.items(): 返回可迭代对象，内部是元组，每个元组内有2个数据
元组数据1是字典的key，元组数据2是字典的value
利用for in 循环遍历字典

'''


dict1 = {'name':'Boer', 'age':20, 'gender':"男"}
for key, value in dict1.items():
    print(key)
    print(value)
    print(f'{key} = {value}')