#需求：复现ATM取钱功能
# 输入密码登录后显示功能，选择查询余额后显示功能，取完钱后显示功能
'''
1.搭建整体框架(复现需求)

2. 确定选择功能界面

3. 封装函数

4. 在需要的位置调用函数

'''


# 0.封装函数
def sel_func():                 
    print('取款')
    print('存款')
    print('显示余额')
#，需要冒号，需要括号，需要缩进下面的代码，以上是定义好的函数，

# 1.框架
print('"登陆成功"')
sel_func()

print('"您的余额是10000000元"')
sel_func()

print('"取了10000元"')
sel_func()
