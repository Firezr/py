#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClassA():
    var1 = '100'

    @classmethod
    def fun1(cls):
        print('var1:' + cls.var1)
        cls.var1 = input('输入 var1 的值')
        print('var1:' + cls.var1)
        cls.var2 = input('输入 var2 的值')
        print('var2:' + cls.var2)

# ClassA.fun1()


class ClassB():
    var1 = '100'

    @classmethod
    def fun1(cls):
        print('var1:' + cls.var1)

ClassB.fun1()
ClassB.var1 = input('输入 var1 的值')
ClassB.fun1()

ClassB.var2 = input('输入 var2 的值')
print(ClassB.var2)