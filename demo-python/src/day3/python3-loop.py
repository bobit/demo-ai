## 对列表内容进行正向排序
str_list = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
str_list.sort()
print(str_list)

## 对列表内容进行反向排序
str_list2 = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
str_list2.sort(reverse = True)
print(str_list2)

## 对列表内容进行反向排序（即可以保留原列表，又能得到已经排序好的列表）
str_list3 = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
result = sorted(str_list3)
result2 = sorted(str_list3, reverse = True)
#print(str_list3)
print(result)
print(result2)
print(sorted(str_list3, reverse = True))
print(sorted(['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou'], reverse = True))
print(['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou'].sort(reverse = True))


## 列表中元素反转排序
### reverse列表反转排序：是把原列表中的元素顺序从左至右的重新存放，而不会对列表中的参数进行排序整理。
str_list4 = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
str_list4.reverse()
print(str_list4)

str_list5 = [1,2,3,5,4]
str_list5.reverse()
print(str_list5)

## 利用步长对序列进行倒序取值
str_list6 = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
print(str_list6[::-1] )