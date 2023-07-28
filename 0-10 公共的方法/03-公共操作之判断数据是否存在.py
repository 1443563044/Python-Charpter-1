'''
实际上判断是否存在就是in 和 not in ，十分简单

in和not in 返回的数据都是True和False

'''''

str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (100, 200, 300, 400)
dict1 = {"age" : 20, 'gender': '男'}
dict1['name'] = 'Tom'  #字典数据增加


#  1.字符串判断
print('a' in str1)   #>>>True
print('a' not in str1)  #>>>False

#  2.列表的判断
print(10 in list1)    #>>>True
print(10 not in list1)   #>>>False

#  3. 元组的判断
print(100 in t1)
print(100 not in t1)

# 4. 字典的判断
print(dict1.keys())
print('name' in dict1.keys())
print('name' in dict1.values())

print(dict1)
print('age' in dict1)