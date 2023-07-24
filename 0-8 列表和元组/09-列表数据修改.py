# 1. 修改指定下标的数据
name_list = ['Boer', 'Tony', 'Lily']
name_list[0] = 'Boer Michel'
print(name_list)

# 2. 逆序 reverse()
name_list1 = [1, 2, 3, 4, 5]
name_list1.reverse()
print(name_list1)

# 3. 排序 和 降序  sort()
#语法： 列表.sort(reverse=False)  True降序 False升序
name_list2 = [1, 2, 3, 4, 5]
name_list2.sort(reverse=False)
print(name_list2)

name_list3 = [1, 2, 3, 4, 5]
name_list3.sort(reverse=True)
print(name_list3)