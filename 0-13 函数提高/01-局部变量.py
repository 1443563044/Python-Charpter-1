# 先定义一个函数，再声明一个变量，然后分别从函数内部访问，函数外部访问，来体验局部变量
def testA():
    a = 100
    print(a)  #  在函数体内部的变量，可以访问到a变量

testA()
# print(a)  #  报错：a变量是函数内部的变量，函数外部无法访问
# 局部变量在函数访问完后，会当局进行销毁
