#注意：else指的是循环正常结束之后要执行的代码，如果使用了break终止循环，else下方缩进的代码将不执行。如下：
#但是使用了continue的话，就是正常结束循环，会执行else缩进的代码
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(f'我：媳妇儿，我错了第{i}次')
    i += 1

else:
    print('媳妇儿原谅我了，真开心，哈哈哈哈')


