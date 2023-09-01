#  把返回值作为一个参数，传递到一个函数中
"""

1. 定义两个函数;
2. 函数test1有返回值50
3. 函数test2把返回值50作为参数传入(定义函数二要有形参)

"""
def test1():
    return 50

def test2(num):
    print(num)

# 具体操作：先得到函数test1的返回值，再把这个返回值传入到函数test2
result = test1()
print(result)  # >>>50
test2(result)