#字符串的常用操作方法有：查找、修改、判断
'''''
子串：字符串中的一部分

语法：
字符串序列.count(子串，开始位置下标，结束位置下标)
字符串序列.index(子串，开始位置下标，结束位置下标)

'''

mystr = 'hello world and itcast and itheima and Python'

# 1.find() 数第几个
print(mystr.find('and')) #12  查找第一个and在哪，并返回数值
print(mystr.find('and', 15, 30)) #23  在第15到30个字符串中查找and，并返回在第几个
print(mystr.find('ands'))  #-1 若不存在子串，则返回-1
print('-----------------------')


# 2.index() 数第几个
print(mystr.index('and'))  #12 结果与find一样
print(mystr.index('and', 15, 30))  #23  结果与find一样
# print(mystr.index('ands'))  #如果是index查找，子串不存在，则报错
print('-----------------------')


# 3.count()  数有几个
print(mystr.count('and', 15, 30))
print(mystr.count('and'))  #3  有3个and，故返回3
print(mystr.count('ands'))  #0  不会报错，有几次返回几次
print('-----------------------')


# 4. rfind()、rindex()  从右侧开始查找罢了
print(mystr.rfind('and'))

# 5.rindex()
print(mystr.rindex('and'))
# print(mystr.rindex('ands')) 一样会报错
