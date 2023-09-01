list1 = []
for i in range(1,3):
    for j in range(3):
        list1.append((i,j))


list2 = [(i,j) for i in range(1,3) for j in range(3)]
print(list2)



# 练手
list3 = ['肉类', '零食', '饮料']
list4 = ['鸡腿', '乐事', '可乐']
dict3 = {list3[i]: list4[i] for i in range(len(list3))}
print(dict3)



counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'Acer':99 }
dict2 = {key: value for key, value in counts.items() if value > 200 }
print(dict2)