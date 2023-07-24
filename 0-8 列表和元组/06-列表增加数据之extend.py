''''
extend():列表结尾追加数据，如果数据是一个序列,
如果是字符串：则会它每个字母拆开来追加
如果是列表：则会把每一个名字分开加入，而不是整个列表加入
'''''

name_list = ['Boer', 'Tony', 'Lily']

#1.extend() 追加字符串
name_list.extend('Tom')
print(name_list)

#2.extend() 追加列表
name_list.extend(['Tom', 'Tod'])
print(name_list)

#和append一样，会在结尾追加数据。
