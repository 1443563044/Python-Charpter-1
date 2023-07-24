'''
所谓判断，只有两个结果，要么真要么假：
返回的结果是布尔型数据类型：True 或 False

语法：字符串序列.startswith(子串，开始位置下标，结束位置下标)

endswith()  同上
'''


# 1.startswith()  判断字符串是否以某个子串开头
mystr = 'hello world and itcast and itheima and Python'
print(mystr.startswith('hello'))
#无论是hel还是hello，返回的结果都是true,因为电脑判断的是字符串(即单个英文字母或者数字)，不是单词

# 2.endswith()
mystr.endswith('python')
print(mystr.endswith('  Python'))
#注意：电脑是区分大小写和空格的





