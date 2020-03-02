# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:13:38 2019

@author: Administrator
"""
"""计数质数  Count Primes
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。"""
"""厄拉多塞筛法:借用列表[1,0]"""
def countPrimes(n):
    if n < 3:
        return 0     
    else:
        # 首先生成了一个全部为1的列表
        output = [1] * n
        # 因为0和1不是质数,所以列表的前两个位置赋值为0
        output[0],output[1] = 0,0
         # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
         # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
        for i in range(2,int(n**0.5)+1): 
            if output[i] == 1:
                output[i*i:n:i] = [0] * len(output[i*i:n:i])
     # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
    return sum(output)

def countPrimes2(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n<3:
        return 0
    nlist=[1]*(n-1)
    nlist[0]=0
    for i in range(2,int(n**0.5)+1):
        if nlist[i-1]==1:
            nlist[i*i-1::i]=[0]*len(nlist[i*i-1::i])
    return sum(nlist)


def countPrimes3(n):
    if n==1 or n==0 or n==2:
        return 0
    nlist=[x for x in range(2,n)]
    j=0
    a=nlist[j]
    while a<n**0.5:
        for i in nlist[j+1:]:
            if i%a==0:
                nlist.remove(i)
        j+=1
        a=nlist[j]
    return len(nlist)
"""算法超时 因为remove时间复杂度远高于修改列表元素"""

print(countPrimes(10))
        