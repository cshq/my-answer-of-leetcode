# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:12:44 2019

@author: Administrator
"""
"""回文数 Palindrome Number
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？"""
"""solution1:string"""
#def isPalindrome(x):
#    if x<0:
#        return False
#    str_x=str(x)
#    if str_x!=str_x[::-1]:
#        return False
#    else:
#        return True
#print(isPalindrome(1221))

"""solution2:not string"""
def isPalinadrome(x):
    if x<0:
        return False
    list_yu=[]
    while x//10:
        j=x%10
        list_yu.append(j)
        x=x//10
    list_yu.append(x)
    if list_yu==list_yu[::-1]:
        return True
    else:
        return False
print(isPalinadrome(12210))
"""solution3 chun math"""
def isPalindrome(x):
    if x<0:
        return False
    temp_x = x;
    palindromeNum = 0
    while temp_x != 0:
        palindromeNum = palindromeNum*10 + temp_x%10
        temp_x /= 10
    return palindromeNum == x
    