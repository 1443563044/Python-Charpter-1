'''''
字符串对齐，就是让你的句子对齐左边、右边、或者中间

有三个函数：
'''

mystr = 'hello'

#1.xx.ljust()
mystr1 = mystr.ljust(10)
print(mystr1 , '.')

#2. xx.rjust()
mystr2 = mystr.rjust(10)
print(mystr2 ,'.')

#3. xx.center() 居中对齐是xxx.center()
mystr3 = mystr.center(10)
print(mystr3 ,'.')


#如果长度大于字符串本身的长度，则可以设置一个填充字符。
#填充字符语法：xxx.ljust(长度,填充字符)