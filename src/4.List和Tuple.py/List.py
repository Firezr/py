#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = [1, 2, 3, 4, 5]

# 通过索引来访问列表
print(name[2])

# 通过方括号的形式来截取列表中的数据
print(name[0:2])
print(name[:2])
print(name[:])
print(name[1:2])
print(name[0:3])

# 通过索引对列表的数据项进行修改或更新
name[1]='22'
print(name)

# 使用 append() 方法来添加列表项
name.append('66')
print(name)

# 使用 del 语句来删除列表的的元素
del name[3]
print(name)


