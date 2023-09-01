# 如果想在两个函数之间访问同一个变量，那么就要用到全局变量
# 定义全局变量a
a = 100
def testA():
    print(a)


def testB():
    print(a)

testA()
testB()