'''
参数的作用：让我们的函数更加的灵活
'''

# 1.固定的数字
# 定义函数
def add_num():
    result = 1 + 2
    print(result)

# 调用函数
add_num()

# 为了更加灵活使用，用户输入什么数据，就将函数传入到定义函数内。

# 2.灵活输入数字

# 定义函数的同时，定义了接收用户数据的参数a和b，a和b是形参（等待接收数据的只是形式上的参数）
def add_num2(a, b):  #叫什么都可以，不一定是a，b
    result1 = a + b
    print(result1)

# add_num2()  #如果不写或者是只写一个（参数丢失），就会报错


# 调用函数时，传入了真实的数据10 和 20 ，真实数据叫做实参

add_num2(10, 20)

""""
以下是一个可以输入数字然后将数字相加的案例：

def num_adds(a, b):
    result = a + b
    print(result)

a1 = int(input("请输入a的值："))
b1 = int(input("请输入b的值："))
print(a1, b1)

num_adds(a1, b1)

"""