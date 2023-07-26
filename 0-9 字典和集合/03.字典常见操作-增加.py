dict1 = {'name':'TOM', 'age':20, 'gender':'男'}

# 1.字典新增：
# 字典序列[key] = 值
# 需求： 增加一个id，值为110
dict1['身份证id'] = 110
print(dict1)

# 2.字典修改（字典是可变类型）
dict1['name'] = '小明'
print(dict1)

#  存在则是修改，不存在则是增加.