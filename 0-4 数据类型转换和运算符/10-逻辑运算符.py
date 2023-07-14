""""
逻辑运算符:
and语法：x and y 与 ，只有x和y都为True的时候，返回的值才为True，即都真才真

or语法： or y 或 ，x或者y有一个是真的，就返回True,都是假的就返回False

not语法： not x 非， 你懂的

"""

a = 0
b = 1
c = 2

#1.x and y   都真才真
#如果其中一个为false，返回False，否则返回True
print(c > b and a > b)
print(a > b and c > b)
print(c > b and b > a)

#2.x or y  一真则真，都假才假
print(a > b or c > b)
print(a > b or b > c)

#3. not 非, 取反义词
print(not False)
print(not a > b) #a大于b假，所以非a > b 就是真
print(not b > a)
print(b > a)



