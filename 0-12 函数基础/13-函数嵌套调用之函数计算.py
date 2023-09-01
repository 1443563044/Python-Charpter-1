# 需求1：任意三个数之和
def sum_num(a, b, c):
    return(a + b + c)

result = sum_num(1, 2, 3)
print(result)

# 需求2：任意三个数的平均数
def average_num(a, b, c):
    #先求和，再除以3
    sumResult = sum_num(a, b, c)
    return sumResult / 3

averageResult = average_num(1, 2, 3)
print(averageResult)
