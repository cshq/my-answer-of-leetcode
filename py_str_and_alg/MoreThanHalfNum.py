# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:27:38 2019

@author: Administrator
"""

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组
{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
'''
#自己的 有问题
'''def f(alist):
    m=[]
    n=len(alist)
    
    for i in range(n):
        count=0
        for j in range(0,n-i):
            if alist[i+j]==alist[i]:
                count=count+1
        m.append(count)
    
    print(m)

f([2,3,2,4,2])
'''
#直接统计
'''def fx(alist):
    for num in alist:
        if alist.count(num)>len(alist)//2:
            return(num)
    return 0


print(fx([1,3,2,4,2,2]))'''

#字典
def MoreThanHalfNum_Solution(numbers):
    dict = {}
    for num in numbers:
        dict[num] = 1 if num not in dict else dict[num]+1
        if dict[num] > len(numbers)/2:
            print (dict)
            return num
    return 0


print(MoreThanHalfNum_Solution([1,3,2,4,2,2,2]))
'''
根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个
数值：数组中的一个数字以及它出现的次数，然后遍历，如果下一个数字等于这个数字，那么次数加一，
如果不等，次数减一，当次数等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，
直到进行到最后，然后再验证最后留下的数字是否出现次数超过一半，因为可能前面的次数依次抵消掉，
最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = 1
        number = numbers[0]
        for i in numbers[1:]:
            if number == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    number = i
                    count += 1
        # 至此选出一个数，但不一定次数过半。最后再迭代一轮，为其记个数。
        sum = 0
        for j in numbers:
            if j == number:
                sum += 1

        return number if sum > len(numbers) // 2 else 0
'''




