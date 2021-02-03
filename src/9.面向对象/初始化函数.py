#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClassA(object):
    var = '100'

    def __init__(self, str):
        print('实例化成功')
        print(str)
    
    def __del__(self):
        print('实例化销毁了')

# 实例化
a = ClassA(12)
del a

