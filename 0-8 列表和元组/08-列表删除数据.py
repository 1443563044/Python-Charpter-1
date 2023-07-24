
#1.del
# 语法： del 目标   或者   del (目标)

'''

例1：
name_list = ['Boer', 'Tony', 'Lily']
del name_list  #删除整个列表
del (name_list) 也可以
print(name_list)
程序会报错

'''

# 例2
name_list1 = ['Boer', 'Tony', 'Lily']
del name_list1[1]  #删除列表第2个
print(name_list1)
print('-----------以上为del函数----------------')

#2. pop() --删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据

# 例子1：
name_list2 = ['Boer', 'Tony', 'Lily']
afterpop = name_list2.pop()  #pop出来的东西是什么？
print(afterpop)
print(name_list2)  #原来的列表还剩下什么
print('-----------pop函数例1----------------')

#例子2：指定下标
name_list3 = ['Boer', 'Tony', 'Lily']
name_list3.pop(1) #pop掉列表中的第2个
print(name_list3)
print('-----------pop函数例2----------------')


# 3. remove(数据)  --删除第一个匹配项
name_list4 = ['Boer', 'Tony', 'Lily']
name_list4.remove('Lily')
print(name_list4)
print('-----------remove函数----------------')

#4. clear() 清空列表
name_list5 = ['Boer', 'Tony', 'Lily']
name_list5.clear()
print(name_list5)
print('-----------clear函数----------------')
