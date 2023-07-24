'''''
删除空白字符有三种，删除左边、删除右边、删除全部空白
'''

mystr = '    hello world and incast and itheima and Python   '
print(mystr)

# 1. lstrip()
new_str = mystr.lstrip()
print(new_str)

#2. rstrip()
new_str1 = mystr.rstrip()
print(new_str1)

# 3. strip()  #删除两侧的空白字符
new_str2 = mystr.strip()
print(new_str2)



