'''
集合是一个数据序列，


1. 创建集合使用{}或者set{},但创建空字典之能使用set(),因为{}用来创建空字典了  dict1 = {}

2.集合的一个特点是：去重  集合里面的数据是没有重复的。

3. 集合打印时没有顺序，所以不支持下标操作

4. 区分字典和集合：
    字典： dict1 = {'name':'TOM', }  存在键值对
    集合:  s1 = {'age', 'name'}  没有键值对

'''

# 1. 创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 20, 30, 40, 50, 10, 50}
print(s2)  #集合数据会自动去重

s3 = set('abcdefg') #利用函数创建集合
print(s3)

# 2. 创建空集合
s4 = set()  #创建空集合只能用set()！！！！
print(type(s4))

s5 = set = {}  #如果用大括号创建出来的则是字典
print(type(s5))
