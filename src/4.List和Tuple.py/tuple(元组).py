#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tuple1=('两点水','twowter','liangdianshui',123,456)
tuple2='两点水','twowter','liangdianshui',123,456
tuple3=()
# 元组中只包含一个元素时，需要在元素后面添加逗号
tuple4=(123,)
tuple5=(123)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)

# 访问元组
print(tuple1[1])
print(tuple2[0])

# 修改元组
list1=[123,456]
tuple1=('两点水','twowater','liangdianshui',list1)
print(tuple1)
list1[0]=789
list1[1]=100
print(tuple1)

# 删除整个元组
del tuple1
print(tuple1)


