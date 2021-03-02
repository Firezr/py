# -*- coding: UTF-8 -*-

sum = lambda num1 , num2 : num1 + num2

print( sum( 1 , 2 ) )


num2 = 100
sum1 = lambda num1 : num1 + num2 

num2 = 10000
sum2 = lambda num1 : num1 + num2 

print( sum1( 1 ) )
print( sum2( 1 ) )