'''
推导式又叫列表生成式
推导式的作用是为了简化代码，美化代码用的

使用的范围是：
列表、集合、字典

'''

#需求：创建一个0-10的列表，分别用while循环和推导式进行书写

# 1. 循环实现
'''
1. 创建空列表
2. 循环将有规律的数据写入到列表
'''

# 1.1 while循环
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# 1.2 for循环
list2 = []
for i in range(10):  #返回的是从0开始到9
    list2.append(i)
print(list2)



# 2. 列表推导式(化简代码，创建或控制有规律的列表)
list3 = [i for i in range(0,10,1)]
print(list3)

'''''
list3 = [i for i in range(0,10,1)]
for前面的i，是for i in range(10)的返回值，即0到9
即列表内生成的是0, 1, 2, 3, 4, 5, 6, 7, 8, 9

'''