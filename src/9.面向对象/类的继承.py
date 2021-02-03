#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClassA(object):
    var = '100'

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account
    
    def get_account(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.var

    @property
    def get_age(self):
        return self._age


class ClassB(ClassA):
    def __init__(self, name, age, account, sex):
        super(ClassB, self).__init__(name, age, account)
        self.sex = sex

if __name__ == '__main__':
    b = ClassB('两点水', 23, 347073565, 1);
    print(b.get_account())

if __name__ == '__main__':
    b2 = ClassB('两点水', 23, 347073565, '男');
    # 打印所有属性
    print(dir(b2))
    # 打印构造函数中的属性
    print(b2.__dict__)
    print(b2.get_name())



class User1(object):
    pass


class User2(User1):
    pass


class User3(User2):
    pass


if __name__ == '__main__':
    user1 = User1()
    user2 = User2()
    user3 = User3()
    # isinstance()就可以告诉我们，一个对象是否是某种类型
    print(isinstance(user3, User2))
    print(isinstance(user3, User1))
    print(isinstance(user3, User3))
    # 基本类型也可以用isinstance()判断
    print(isinstance('两点水', str))
    print(isinstance(347073565, int))
    print(isinstance(347073565, str))