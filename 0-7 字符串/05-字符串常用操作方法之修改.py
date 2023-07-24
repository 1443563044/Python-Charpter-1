'''''
修改就是运用函数的方式修改字符串中的数据

'''

mystr = 'hello world and itcast and itheima and Python'

# 1.replace() 字符串序列.replace(旧子串, 新子串,替换次数)
# 需求：运用replace() 把and替换成he
new_str = mystr.replace('and', 'he')  #全部替换
print(new_str)
new_str1 = mystr.replace('and', 'he' , 1)  #替换一次and
print(new_str1)
new_str2 = mystr.replace('and', 'he' , 10)  #超过的话，就是替换所有
print(new_str2)
print('-----------------------')




#2.split()  语法：字符串序列.split(分割字符, num)
list1 = mystr.split('and') #全分割
print(list1)  #分割，返回一个列表，会丢失分割符号
list2 = mystr.split('and', 2)   #分割两次
print(list2)
print('-----------------------')



#3. join()  --合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
print('停在这里'.join(mylist)) #列表三个字符串，合并成了一个大字符串
print('-----------------------')
# 不太明白


# 4.将数据是否可以改变划分为： 可变类型 和 不可变类型
# 注意！！调用了replace函数后，发现原字符串的数据并没有做到修改，修改后的数据是replace的返回值
# 说明了 字符串是不可变数据类型，证明和方法如下：
mystr = 'hello world and itcast and itheima and Python'
print(mystr.replace('and', 'he', 2))
print(mystr)
print('-----------------------')