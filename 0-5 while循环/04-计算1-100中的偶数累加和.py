# 需求： 1-100偶数累加 -- 2 + 4 + 6 + ... + 100 = 结果 输出结果
'''''
1. 准备累加的数字，设置变量，从1开始，结束为100，增量为1
2. 准备保存结果的变量result
3. 循环加法运算 -- 如果是偶数才做加法(即和2取余数为0，用if条件语法)
4. 输出结果
5. 验证结果(缩小数字的思维)
'''

i = 1
result = 0
while i <= 100:
    if i % 2 == 0: # 条件语句 ，判断是否相加
        result += i
    i += 1
print(result)

#提示：可以利用Debug测试，看每一步变量的值。