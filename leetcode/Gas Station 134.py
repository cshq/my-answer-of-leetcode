# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:24:52 2019

@author: THTF
"""
"""在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

	如果题目有解，该答案即为唯一答案。
	输入数组均为非空数组，且长度相同。
	输入数组中的元素均为非负数。

示例 1:
输入: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:
输入: 
gas  = [2,3,4]
cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。"""

"""两重循环，效率低"""
def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    for i in range(len(gas)):
        flag=True
        cur_gas=gas[i]
        for end in range(i,i+len(gas)):
            end=end%len(gas)
            if cur_gas<cost[end]:
                flag=False
                break
            cur_gas=cur_gas+gas[(end+1)%len(gas)]-cost[end]
        if flag==True:
            return i
    return -1

#如果没有flag=True来界定的话，只能把return放在第二层循环外面，这样会导致无论如何都会第二次循环结束就会
#    返回i，而这显然不对，因此要用个flag.
    
"""一遍循环"""
def canCompleteCircuit2(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    c_gas=0
    location=0
    if sum(gas)<sum(cost):
        return -1
    for i in range(len(gas)):
        c_gas=c_gas+gas[i]-cost[i]
        if c_gas<0:
            location=i+1
            c_gas=0
    return location
#如果到不了i，则从i+1另起炉灶。因为到不了i（要么再i-1还有油或者没油），之前就没有点能到i。所以i+1另起炉灶
#当然总的不如消耗的，也不行，这就是的第一个if。
