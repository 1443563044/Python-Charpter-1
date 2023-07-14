"""""
and运算符，只要有一个数字为0，则结果返回为0，否则结果为最后一个非0数字
print(1 and 0)  >>>0
print(0 and 1)  >>>0
print(1 and 2)  >>>2
print(2 and 1)  >>>1
"""

print(0 and 1)
print(1 and 0)
print(1 and 2)
print(2 and 1  , end = "\n \n")


"""""

or运算符，只有所有值为0才为0，否则返回第一个非0数字
print(1 or 0)  >>>1
print(0 or 1)  >>>1 #返回第一个非0数字
print(1 or 2)  >>>1
print(2 or 1)  >>>2
"""

print(1 or 0)
print(0 or 1)
print(1 or 2)
print(2 or 1)
