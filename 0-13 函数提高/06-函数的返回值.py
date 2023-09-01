"""
如果一个函数有两个return，程序在执行完第一个return之后将不再执行第二个return
是因为return可以退出当前函数，导致return下方的代码不执行

"""
# 需求： 一个函数有两个返回值，分别是1和2
def return_num():
    return 1
    return 2

result = return_num()
print(result)

# 结论：一个函数如果有多个return，只执行第一个return。

# 正确做法：
def return_num1():
    # return 1, 2  # 返回的是元组
    # return (1, 2)
    # return [100, 200]
    return {'name':"Boer", "age":20}

result2= return_num1()
print(result2['name'],'，','已经',result2['age'],end='')

"""
注意:
1. return a, b的写法。当返回多个数据的时候，默认是元组类型
2. return后面可以连接列表、元组或字典，以返回多个值
"""