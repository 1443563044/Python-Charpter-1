str1 = 'itheima'
for i in str1:
    #当某些条件成立时退出循环进入下一个循环
    if i == 'e':
        continue   #遇到e就退出循环,不执行print(i)
    print(i)