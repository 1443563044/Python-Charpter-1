mystr = 'hello world and itcast and itheima and Python'

# 1.isalpha(): 判断字符串是否全是字母
print(mystr.isalpha())  #因为mystr字符串中含有空格，所以返回的是False
print('--------------')

# 2.isdigit():  判断是否全是数字
print(mystr.isdigit())
mystr1 = '12345'
print(mystr1.isdigit())
print('--------------')

# 3.isalnum():  非空字符串中都是数字或字母或组合
mystr2 = '12345'
print(mystr2.isalnum())

print(mystr.isalnum())  #返回false,因为该字符串中包括了空白字符(空格)

mystr3 = '123abc'
print(mystr3.isalnum())
print('--------------')

# 4.isspace() 判断是否都是空白
print(mystr.isspace())
mystr4 = '    '
print(mystr4.isspace())