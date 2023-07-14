num1 = 1
str1 = '10'
#1. float()  -- 将数据类型转换成浮点型
print(type(num1))
print(num1)
print(type(float(num1)))  #转换成浮点型
print(num1)  #两种不同格式的变量打印，显示出来的也不同
print(float(num1))
print('%.6f ' % num1)

#2. str() -- 将数据转换成字符串型
print(type(str(str1)) ,end='第十二行\n')


#3. tuple() -- 将一个序列转换成元组
#注意！列表是中括号，元组是小括号
list1 = [10, 20, 30]  #这是列表序列
print(type(tuple(list1))) #将列表转换成元组

#4. list() -- 将一个序列转换成列表
t1 = (100, 200, 300) #这是元组序列
print(t1)
print(list(t1)) #转换成tuple了

# 5. eval() --计算在字符串中的有效Python表达式，并返回一个对象
#注意，这个函数可以自动识别字符串，并返回相应的对象。(例如字符串1.1，使用后会自动转成浮点型)
str2 = '1'  #整数型
str3 = '1.1'  #浮点型
str4 = '(1000, 2000, 3000)'  #元组型
str5 = '[1000, 2000, 3000]'  #列表型

#转换前：
print(type(str2))
print(type(str3))
print(type(str4))
print(type(str5))
#转换后：
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
