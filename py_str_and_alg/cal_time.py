# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:57:31 2019

@author: Administrator
"""
import timeit
def pow():
    for a in range(1000):
        for b in range(1000):
            c=1000-a-b
            if c**2==a**2+b**2:
                return(a,b,c)

time1=timeit.timeit("pow()","from __main__ import pow",number=1000)
print(time1)
#
#
#import timeit
# 
 
## 待测试的函数
#import timeit
#def add():
#    return sum(range(111))
# 
# 
## stmt 需要测试的函数或语句，字符串形式
## setup 运行的环境，本例子中表示 if __name__ == '__main__':
## number 被测试的函数或语句，执行的次数，本例表示执行100000次add()。省缺则默认是10000次
## 综上：此函数表示在if __name__ == '__main__'的条件下，执行100000次add()消耗的时间
#t = timeit.timeit("add()","from  __main__ import add", number=100000)
#print(t)
