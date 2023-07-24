#需求：注册邮箱，用户输入一个账号名>>判断用户是否存在
# >>若存在，提示换一个，若不存在，提示可以注册

''''
1.用户输入账户
2.用if...else判断

'''

name_list = ['Boer', 'Tony', 'Lily']

name = input('请输入你的邮箱账户：')

if name in name_list:
    #若存在，不能注册
    print(f'您输入的名字是{name}，此用户名已存在')
else :
    #若不存在，可以注册
    print(f'您输入的名字是{name}，可以注册')
