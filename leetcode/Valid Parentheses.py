# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:05:16 2019

@author: Administrator
"""

""" 有效的括号 Valid Parentheses
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true"""
"""solution:using stack"""
def ValidParentheses(s):
    d={')':'(',']':'[','}':'{'}
    stack=[]
    for i in s:
        if i in d.values():
            stack.append(i)
        else:
            if stack==[]:
                return False
            elif d[i]!=stack.pop():
                return False
    if stack:
        return False
    else:
        return True

print(ValidParentheses("()[]{}"))