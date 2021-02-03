# -*- coding: utf-8 -*-

# 默认参数的值是不可变的对象，比如None、True、False、数字或字符串
def print_info( a , b = [] ):
    print(b)
    return b 

result = print_info(1)
result.append('error')
print_info(2)


# 测试同一性, 判断是否有值输入
_no_value =object()

def print_info2( a , b = _no_value ):
    if b is _no_value :
        print('b 没有赋值')
    return


def print_user_info( name , age , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = '..')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数
print_user_info( '两点水' , 18 , '女')
print_user_info( '三点水' , 25 )


# 关键字参数
def print_user_info2( name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数
print_user_info2( name = '两点水' ,age = 18 , sex = '女')
print_user_info2( name = '两点水' ,sex = '女', age = 18 )


# 不定长参数
def print_user_info3( name ,  age  , sex = '男' , * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info3( '两点水' ,18 , '女', '打篮球','打羽毛球','跑步')

# *hobby是可变参数，且 hobby其实就是一个 tuple （元祖），**hobby是关键字参数，且 hobby 就是一个 dict （字典）

def print_user_info4( name ,  age  , sex = '男' , ** hobby ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info4( name = '两点水' , age = 18 , sex = '女', hobby = ('打篮球','打羽毛球','跑步'))


# 强制关键字参数 / 只接受关键字参数
def print_user_info5( name , *, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数
print_user_info5( name = '两点水' ,age = 18 , sex = '女' )

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
#print_user_info( '两点水' , 18 , '女' )
print_user_info5('两点水',age='22',sex='男')