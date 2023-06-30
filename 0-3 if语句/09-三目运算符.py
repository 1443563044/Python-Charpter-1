'''
语法
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
'''

a = 1
b = 2
#如果a>b则输出a，a不大于b则输出b：
c = a if a > b else b
print(c)

#需求：有两个变量比较大小。如果 变量1大于变量2 执行 变量1-变量2 ：否则 变量2-变量1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)

# 完整版是：
if aa > bb:
    cc = aa - bb
    print(cc)
else:
    cc= bb - aa
    print(cc)

