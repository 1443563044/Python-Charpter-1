name = '老衲'
age = 80

# 我的名字是x，今年x岁了
# %s语法：
print("我的名字是%s，今年%s岁了" % (name, age))

# 语法 f‘｛表达式｝’
print(f'我的名字是{name}，今年{age}岁了')
print(f'我的名字是{name}，今年{age+1}岁了')

#区别：f'{}'更加简洁