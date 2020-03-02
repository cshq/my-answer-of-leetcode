# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:45:14 2019

@author: Administrator
"""
#输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
#则打印出这三个数字能排成的最小数字为321323。
def PrintMinNumber(numbers):
        a=list(map(str,numbers))
        for i in range(len(a)):
            for j in range(1,len(a)-i):
                if a[i]+a[i+j]>=a[i+j]+a[i]:
                    a[i],a[i+j]=a[i+j],a[i]
        
        result=''.join(a)
        print(int(result))


PrintMinNumber([3,5,1,4,2,8,14])
