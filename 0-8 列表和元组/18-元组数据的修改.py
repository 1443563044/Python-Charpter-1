t1 = ('aa', 'bb', 'cc', 'bb')
# t1[0] = 'aaa'  程序会报错，因为元组内的数据不能修改


t2 = ('aa', 'bb', ['cc', 'dd'])
print(t2[0])
print(t2[1])
print(t2[2])

print(t2[2][0])  #如果是s元组里面的列表，是支持修改的

#工作中，元组的数据尽量不做修改