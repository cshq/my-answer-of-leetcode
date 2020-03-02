# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:43:41 2019

@author: THTF
"""

import re
def detection(text):
    if (len(text)<8):
        return False
    number1=re.compile(r'\d+')
    if number1.search(text)==None:
        return False
    number2=re.compile(r'[A-Z]+')
    if number2.search(text)==None:
        return False
    number3=re.compile(r'[a-z]+')
    if number3.search(text)==None:
        return False
    return True

text=input("Get the password that you want to set\n")
if detection(text):
    print ("The password is the strong password.")
else:
    print("Warning:The password is not the strong password.")