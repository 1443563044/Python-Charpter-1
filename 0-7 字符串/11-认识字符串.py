# 1.单引号和双引号数据类型

a = 'hey'
print(a)
print(type(a))

b = "heyy"
print(b)
print(type(b))

# 2.三引号(与多行注释一样)
e = '''i am TOM'''
print(type(e))

f = """"I am TOM"""
print(type(f))


# 3.一种全新的
f1 = """I am TOM,
it's a pleasure to get aquainted with you"""
print(f1)
print(type(f1))
#即便在中途换行，也不会报错

# 4.是否能输入 I'm
c = "I'm TOM，" \
    ""
print(c)
print(type(c))

# d = 'I'm TOM'
# print(d)
# print(type(d))
#使用双引号可以，但是使用单引号的话，机器会报错，那么，如何解决呢？
#可以通过输入转义字符
d = 'I\'m TOM' #使用了转义符号，把原来的引号，变成了英语里面的引号
print(d)
print(type(d))