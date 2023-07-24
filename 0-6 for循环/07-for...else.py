#情况1
str = "itheima"
for i in str:
    print(i)
else:
    print('结束循环-------以上为情况1')


#情况2
str = "itheima"
for i in str:
    if i == 'e':
        print('break遇到了字母e，终止所有循环，不再继续打印--------以上为情况2')
        break
    print(i)
else:
    print('结束循环')


#情况3
str = "itheima"
for i in str:
    if i == 'e':
        print('continue遇到了字母e，不打印e，但继续打印后面的')
        continue
    print(i)
else:
    print('结束循环--------以上为情况3')