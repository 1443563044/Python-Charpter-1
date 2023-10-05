'''
函数调用，通过''键=值''的形式加以指定，可以让函数更加清晰、容易使用，同时也清楚了参数的顺序需求

调用函数时，如果同时存在位置参数和关键字参数时，位置参数必须在关键字参数的前面。
Tip:关键字函数之间不存在先后顺序

'''

def user_info1(name, age, gender):
    print(f'我的名字是{name},我的年龄是{age},我的性别是{gender}')

#调用函数传参(Key=Value形式，即age=20这样子输入)
user_info1('BOER', age=20, gender='男')
user_info1('BOER',  gender='男', age=20) #即便打乱了参数的顺序，还是会按照顺序进行传递参数，不会报错

#位置参数必须在关键字参数的前面
#报错：user_info1(gender='男', age=20, 'BOER')
