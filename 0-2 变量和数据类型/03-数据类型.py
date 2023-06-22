"""
1.储存不同类型的数据

2.验证这些数据是什么类型---type(数据)

3.print(type(xx))
int(整数型)
float(浮点型)
"""

#整数型 int
num1 = 1
type(num1)
print(type(num1))

#浮点型 float
num2 = 1.1
type(num2)
print(type(num2))

#字符串(数据要带引号) str
a = '你好'
print(type(a))


#布尔型（在判断时使用） 只有两个取值
b = True
print(type(b))

#列表型 list(用中括号)
c = [10, 20, 30]
print(type(c))

#元组型 tuple
d = (10, 20, 30)
print(type(d))

#集合 set
e = {10, 20 ,30}
print(type(e))

#字典 dict
f = {'name': 'TOM', 'age': 18}
print(type(f))