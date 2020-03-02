# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:04:37 2019

@author: THTF
"""

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    dp=[0]*len(s)
    if s[0]=='0':
        return 0
    if len(s)==1:
        return 1
    dp[0]=1
    if s[1]=='0' and int(s[:2])<=26:
        dp[1]=1
    if s[1]=='0' and int(s[:2])>26:
        dp[1]=0
    if s[1]!='0' and int(s[:2])<=26:
        dp[1]=2
    if s[1]!='0' and int(s[:2])>26:
        dp[1]=1
    for i in range(2,len(s)):
        if (int(s[i])+10*int(s[i-1]))<=26:
            if s[i]=='0' and s[i-1]!='0':
                dp[i]=dp[i-2]
            elif s[i]=='0' and s[i-1]=='0':
                return 0
            elif s[i]!='0' and s[i-1]=='0':
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]+dp[i-2]
        elif (int(s[i])+10*int(s[i-1]))>26 and s[i]=='0':
             dp[i]=0
        elif (int(s[i])+10*int(s[i-1]))>26 and s[i]!='0':
            dp[i]=dp[i-1]
    return dp[-1]
"""动态规划，思路简单，就是corner case太多"""
"""for 循环里可以以是否为0为第一个层判断条件，可能简单点"""

"""https://leetcode-cn.com/problems/decode-ways/solution/dong-tai-gui-hua-tu-jie-by-nfgc/"""