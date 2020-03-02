# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:13:53 2019

@author: Administrator
"""
"""报数 Count and Say
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串"""

"""solution1 思路：递归的思路
如果n=1，返回字符串'1'
得到countAndSay(n-1)的字符串， 从字符串的第一位开始处理，辅助一个计数值count_num：表示重复的字符数，以及num：前一位的字符
如果当前位与前一位一样，那么count_num加一；
如果当前位于前一位不一样，那么需要把前面的字符输出，即追加 count_num+num的字符串；
最后，为了保证最后一位的信息也添加进去，增加了一步：strs+= count_num + char的操作。
最后，返回字符串strs即可。"""
def countAndSay(n):
    if n == 1:
        return '1'
    count_num = 0
    num = ''
    strs = ''
    for char in countAndSay(n-1):
        if char != num:
            if count_num>0:
                strs += str(count_num) + num
#       也可以没有if coun_sum>0的判断。但是这就要求前面num=countAndSay[0]，时间复杂度增加 导致不AC
            count_num = 1
            num = char
        else:
            count_num += 1
    strs += str(count_num) + char
    return strs
print(countAndSay(4))

"""solution2:也是递归 但是调用了太多的目标function还有索引，所以时间复杂度太高 不适用"""
def countAndSay2(s):
    if s==1:
        return "1"
    if s==2:
        return"11"
    count=1
    strs=''
    for i in range(1,len(countAndSay(s-1))):
#        if s==1:
#            return "1"
        if countAndSay(s-1)[i]==countAndSay(s-1)[i-1]:
            count+=1
        else:
            strs=strs+str(count)+countAndSay(s-1)[i-1]
            count=1
    strs=strs+str(count)+countAndSay(s-1)[i]
    return strs
print(countAndSay2(9))

                
            