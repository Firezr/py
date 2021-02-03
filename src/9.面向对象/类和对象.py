#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClassA():
    var = '100'

    @classmethod
    def fun1(cls):
        print('var:' + cls.var)

# ClassA.fun1()


class ClassB(object):
    var = '100'

    def fun1(self):
        print('var:' + self.var)


def fn(self):
    print('new fn')

# 实例化
b = ClassB()
b.fun1()
# print(b.var)

ClassB.fun1 = fn
b.fun1()

# ClassB.var = '200'
# print(b.var)


# 实例化
c = ClassB()
c.fun1()
# print(c.var)
# c.var = 300
# print(c.var)
# print(ClassB.var)


# 类的属性/方法改变，实例跟着改变
# 实例的属性改变，不影响类；实例的方法无法改变（修改会报错）