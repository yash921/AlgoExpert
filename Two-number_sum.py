#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:57:21 2020

@author: root
"""
############################Two-Number Sum###################



def twoNumberSum(array,targetSum):
    """  
    O(n^2) time and O(1) space
    """
    for i in  range(len(array)-1):
        first_Number = array[i]
        for j in range(i+1,len(array)):
            second_Number = array[j]
            if first_Number + second_Number == targetSum:
                return [first_Number,second_Number]
    return []





###############Using Hashing#############################
    

def twoNumberSum(array,targetSum):
    """
    time=O(n), space=(n)
    """
    nums={}
    for num in array:
        potentialSum = targetSum - num
        if potentialSum in nums:
            return [potentialSum,num]
        else:
            nums[num]=True
    return []


############Using left and right pointer#################
    

def twoNumberSum(array,targetSum):
    """
    time = O(nlogn) | space = (1)
    """
    array.sort()
    leftPointer = 0
    rightPointer = len(array) - 1
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
            return [array[leftPointer],array[rightPointer]]
        elif currentSum < targetSum:
            leftPointer+=1
        elif currentSum > targetSum:
            rightPointer-=1
    return []
    

array = list(map(int, input().split()))
targetSum = int(input())
print(twoNumberSum(array,targetSum))

