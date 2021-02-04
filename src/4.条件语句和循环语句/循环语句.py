# -*- coding: utf-8 -*-

for letter in 'Hello 两点水':
    print(letter)

dict = {1:11,2:22,3:33}
for i in dict:
    print(i, dict[i])


for i in range(0, 3):
    print(i)

# 从 0 数到 10（不取 10 ），每次间隔为 2 
for i in range(0,10,2):
    print(i)

print(range(0,10,2))


count = 1
sum = 0

while count <=100:
    sum += count
    count = count+1
print(sum)


count = 1
sum = 0
while (count <= 100):
    if ( count % 2 == 0):  # 双数时跳过输出
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print(sum)

# for … else ，也有 while … else
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 是一个合数' % num)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
