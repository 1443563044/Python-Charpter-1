''''
enumerate(可遍历对象，start=0)
start参数是用来设置遍历数据的下标起始值，默认是0

'''

list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i)

'''
>>>
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')

'''''
list2 = ['小红', '小明', '小军', '小李', '小磊']
print(list2)
for i in enumerate(list2, start=1):  #返回的元组，起始值为1
    print(i)


#返回的结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据