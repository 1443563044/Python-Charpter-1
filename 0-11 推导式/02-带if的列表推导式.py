#创建一个1-10的偶数推导式,有三种实现方式

# 1.简单列表推导式 range
list1 = [i for i in range(0, 10, 2 )]
print(list1)


# 2. for循环加if 创建有规律的列表
list2 = []
for i in range(0, 10, 1):
    if i % 2 == 0:
        list2.append(i)
print(list2)


# 3.把for循环配合if的代码 改写 带if的列表推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)

#新语法，列表内的带if的列表推导式。去掉所有的冒号标点，和回车换行
