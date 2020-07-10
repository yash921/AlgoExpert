#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:43:35 2020

@author: root
"""

def firstNotRepeatingCharacter(s):
    """
    Time O(n^2) | Space O(1)
    """
    for i in range(len(s)):
        seenDuplicate = False
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                seenDuplicate = True
                break
        if seenDuplicate != True:
            return s[i]
    return "_"


#####################################


def firstNotRepeatingCharacter(s):
    """
    Time O(n) | Space O(n)
    """
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for j in d:
        if d[j] == 1:
            return j
    return '_'
        
    
        
print(firstNotRepeatingCharacter("ababcdd"))
            