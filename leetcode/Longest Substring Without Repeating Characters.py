# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:53:33 2019

@author: Administrator
"""

"""
 Longest Substring Without Repeating Characters
 无重复字符的最长子串
 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串
"""
def lengthOfLongestSubstring(s):
        start=0
        maxlength=0
        sub_dic={}
        for i in range(len(s)):
            if s[i] in sub_dic and start<=sub_dic[s[i]]:
                start=sub_dic[s[i]]+1
            else:
                maxlength=max(maxlength,i-start+1)
            sub_dic[s[i]]=i
#        sub_dic[s[i]]应该放在循环外面，而不仅仅在else里（如果不在则增加，如果在则更新位置）
        return maxlength
print(lengthOfLongestSubstring('pwmgswknwp'))
            