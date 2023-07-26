''''
查找字典中的数据常见有以下几种方式：
1. 直接查找，语法是  字典序列['key'] 存在返回对应值，不存在则报错

2. get,语法是  字典序列.get.('key','默认值') 存在则返回key对应的值，不存在则返回默认值，不存在且无默认值则返回none

3. keys 语法是   字典序列.keys()  返回字典内所有的key

4. values  语法是  字典序列.value() 返回字典内所有keys对应的值

5.  items  语法是  字典序列.items()  以元组的形式返回key和对应的key值

'''



dict1 = {'name': '小明', 'age':20, 'gender':'男'}

# 1.key值的查找
print(dict1['name'])  #key存在时，返回对应的值
# print(dict1['id'])   不存在时，报错！
print('---------------------')


# 2.1 get()
#语法： 字典序列.get(key,默认值)
#注意：如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回NONE
#例子:
print(dict1.get('name'))  #会返回key所对应的值
print(dict1.get('names'))   #如果key没有值可以返回，那就返回none
print(dict1.get('names', '小红'))  #如果默认值存在，则返回默认值
print('---------2.1 get---------')


# 2.3 keys() 查找字典中所有的key，返回可迭代的对象，返回key
print(dict1.keys())  # >>>dict_keys(['name', 'age', 'gender'])
print('---------2.2 keys---------')


# 2.4 values()  查找字典中所有的key，返回可迭代的对象，返回key对应的值
print(dict1.values())  # >>>dict_values(['小明', 20, '男'])
print('---------2.3 values---------')


# 2.5 items()  查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，第一位是key，第二位是key对应的value
print(dict1.items())
print('---------2.4 items---------')

