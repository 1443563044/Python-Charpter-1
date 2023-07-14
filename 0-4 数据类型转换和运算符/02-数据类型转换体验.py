"""
1.input

2.检测input的数据类型 str

3.使用int()转换数据类型

4.检测是否转换成功
"""

num = input('请输入数字：')
print(num)

type(num)
print(type(num)) #检测为str

int(num)  #将其转为int整数型
print(type(int(num)))  #看看是不是int