# 需求：函数嵌套打印五条横线

def print_line():
    print('-' * 20)

def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1

print_lines(5)