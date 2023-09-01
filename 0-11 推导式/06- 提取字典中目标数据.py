'''''
提取字典中，想要的数据，并且返回
'''

# 需求： 提取电脑台数大于等于200的品牌
# 获取所有键值对数据，判断v值大于等于200，返回一个字典数据

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'Acer':99 }
print(counts.items())  #>>>以元组的形式返回数据（复习）

# 用for循环实现以上需求：
for key, value in counts.items():
    if value >= 200:
        dict1 = {key: value}  #>>>将卖出数量大于200台的电脑存储到字典中
        print(dict1)


#用推导式实现以上需求：午安宝
dict2 = {key: value for key, value in counts.items() if value > 200 }
print(dict2)



# 注意，这里的key和value只是一个随机随机变量，并不是字典内的key和value
for k, v in counts.items():
    if v >= 200:
        dict1 = {k: v}
        print(dict1)