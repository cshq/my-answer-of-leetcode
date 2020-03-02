# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:31:26 2019

@author: THTF
"""

def getHint(secret, guess):
    from collections import Counter
    countA=0
    countB=0
    s1=[]
    s2=[]
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            countA+=1
        else:
            s1.append(secret[i])
            s2.append(guess[i])
    c_s1=Counter(s1)
    c_s2=Counter(s2)
    for k in c_s1:
        if k in c_s2:
            countB+=min(c_s1[k],c_s2[k])
    return "{}A{}B".format(countA,countB)
                    
#Counter类还是挺方便的
getHint("1807","7810")