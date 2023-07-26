''''
遍历字典的元素，实质上就是遍历每一个键值对，
并且以元组的形式返回
'''

dict1 = {'name': 'Boer', 'age': 20, 'gender': '男'}
print(type(dict1['name']))
print(type(dict1['age']))  #返回key所对应的value

for item in dict1.items():
    print(item)
