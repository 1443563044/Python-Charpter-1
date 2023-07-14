"""
1. 书写input
    input('提示信息')

2.观察特点
    2.1 程序遇到input，会等待用户输入
    2.2 接受input存变量
    2.3 input接收到的数据类型是字符串
"""

password = input('请输入您的密码：')
print(f'您输入的密码是{password}')

print(type(password))
