''''
字典的删除有两种：
第一种是del，第二种是clear
'''

dict1 = {'name': '小明', 'age':20, 'gender':'男'}

# 1.del()  删除整个字典或者是指定键值对
# del(dict1)  #删除整个字典
print(dict1)  #删除后，字典dict1没有了，无法打印，程序会报错


del dict1['name']
# del dict1['names']  这个K的值不存在，所以无法删除，程序报错
print(dict1)

# 2.clear()  删除字典的key，但是保留字典
dict1.clear()
print(dict1)