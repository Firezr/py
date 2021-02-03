#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClassA():
    var1 = '100'

    @classmethod
    def fun1(cls, age):
        print('我是 fun1' + cls.var1)
        print('age', age)

print(ClassA.var1)
ClassA.fun1(18)