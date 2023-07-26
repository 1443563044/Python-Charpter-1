'''''
1.remove() 删除集合中指定的数据，数据不存在则报错


2.discard()  删除集合中指定的数据，如果数据不存在也不会报错


3.pop()  删除集合中随机一个数据


'''
# 1. remove()
s1 = {10, 20, 30, 40, 50}
s1.remove(10)
print(s1)

# s1.remove(10)  #已经删除了10，remove()删除不存在的值会报错

# 2. discard()
s2 = {10, 20, 30, 40, 50}
s2.discard(10)
print(s2)
s2.discard(10)  #不会报错
s2.add(10)

# pop() 随机删除一个数据并返回这个数据
del_num = s2.pop()
print(del_num)
print(s2)