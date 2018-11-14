import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

#!/usr/bin/python
# -*- coding: UTF-8 -*-

x="a"
y="b"
# 换行输出
print(x),
print(y),
print(x,y)


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
print(list)