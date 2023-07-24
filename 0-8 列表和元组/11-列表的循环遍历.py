''''
列表的循环遍历，通俗来说是一次打印列表中的各个数据

比如说：[j, k, l, m]
循环遍历就是将他们一次打印出来

'''

#利用while循环
name_list = ['Boer', 'Tony', 'Lily']
i = 0
while i < len(name_list):
    if i == 1:
        print('不打印Tony，继续打印下面的')
        i += 1
        continue
    print(name_list[i])
    i += 1

