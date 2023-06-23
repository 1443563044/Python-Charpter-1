"""
1.print()里面默认的结束符是\n，所以，
  多个print()时，会自动换行,例如下面例子
2.语法为print("xxxx", end="xxx")
3.end="xx"
"""

#1.不使用结束符，默认就是\n
print('她说："我叫...."')
print('"你叫什么？"他歪着头问道')

#2.使用结束符\n
print('halo', end="\n")
print('world')

#3.使用制表符\t
print('halo', end="\t")
print('world')

#4.使用自己需要的标点作为结束符
print('我想', end="...")
print('睡觉', end="。\n") #符号后面用了换行符，也可以进行换行

#5. 不使用任何符号
print('她说："我叫...."', end = '')
print('"你叫什么？"他歪着头问道')

