''''
元组特点：定义元组使用！小括号！ ， 且逗号隔开各个数据，数据可以是不同的数据类型（int、str、tuple...）

'''

# 1.多个数据元组
t1 = (10, 20, 30)
print(type((t1)))

# 2.单个数据的元组
t2 = (10, )
print(type((t2)))

# 3. 如果单个数据不加逗号
t3 = (10)
print(type(t3))

t4 = ('Boer')
print(type(t4))

t5 = ('Boer', )
print(type(t5))

#列表则不同，列表在最后不需要加逗号