''''
break:当某些条件成立时，结束循环
循环吃5个苹果，吃完第三个吃饱了，第四和第五不吃了(停止执行)
判断方法:可以是小于4执行，或者是>3停止

'''
#注意及时复习f"{}"语法
i = 1
while i <= 5:
    print(f'吃了第{i}个苹果')
    i += 1


#条件： 如果吃到4 或者 >3， 打印吃饱了不吃了
i2 = 1
while i2 <= 5:
    if i2 == 4:
        print("吃饱了，不吃了")
        break  #当i=4时终止循环
    print( f'吃了第{i2}个苹果')
    i2 += 1

#注意及时复习f"{}"语法,格式化字符串。