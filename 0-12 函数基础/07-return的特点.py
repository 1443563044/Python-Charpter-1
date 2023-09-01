'''
自行在上一节中用debug测试

'''

def buy():
    return '烟'  # return这一行后面的代码不执行
    print('OK')

goods = buy()
print(goods)

buy()  # 这样也不执行

''''
return的作用：
1. 负责函数返回值
2. 退出当前函数：导致return下方的所有代码(函数体内部)不执行
'''