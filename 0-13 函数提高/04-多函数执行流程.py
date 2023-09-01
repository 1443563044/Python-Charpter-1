# 共用全局变量
# 1. 定义全局变量; 2. 定义两个函数 3. 函数test1修改全局变量:函数test2访问全局变量

glo_num = 0

def test1():
    global glo_num
    #修改全局变量
    glo_num = 100

def test2():
    print(glo_num)

print(glo_num)

test1()  # 函数test1一调用，glo_num就会变成100

test2()

print(glo_num)  #此时再打印，glo_num就会变成100