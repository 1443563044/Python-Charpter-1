age = 20.0000
print('我今年%02d岁' % age)
print(type(age))

name = '卧室'
print('该房间的属性是%s' % name)
print(type(name))

size = 300.5


room1_num = 9785
room2_num = 9
print('这间房的编号是%05d' %room1_num)
print('这间房的编号是%03d' %room2_num)

print('这间房的编号是%d,属性是%s' % (room1_num, name))
print('下一间房的编号是%d,属性是%s' % (room1_num+1, name))

print('入住客户名字是%s,房间编号是%05d,,面积是%.2f' %(name, room1_num, size))


print(f'入住客户的名字是{name},房间的编号是{room1_num}')


print('halo\nworld')
print('\tabcd')

print('我想', end = "...")
print('和你一起去旅游', end = "。")