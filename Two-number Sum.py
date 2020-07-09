#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:57:21 2020

@author: root
"""
############################Two-Number Sum###################

#Approach 1: Brute Force

#The brute force approach is simple. Loop through each element xxx and 
#find if there is another value that equals to target−xtarget - xtarget−x.


def twoNumberSumBruteForce(array,targetSum):
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

#Complexity Analysis

#Time complexity : O(n2)O(n^2)O(n2). For each element, 
#we try to find its complement by looping through the rest of array which takes O(n)O(n)O(n) time.
#Therefore, the time complexity is O(n2)O(n^2)O(n2).

#Space complexity : O(1)O(1)O(1)



###############Using Hashing#############################
#Approach 2: Two-pass Hash Table   

def twoNumberSumUsingHasing(array,targetSum):
    """
    time=O(n), space=(n).
    Space complexity can be used to speed up the Time complexity.
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
    

def twoNumberSumUsingPointer(array,targetSum):
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
print(twoNumberSumBruteForce(array,targetSum))
print(twoNumberSumUsingHasing(array,targetSum))
print(twoNumberSumUsingPointer(array,targetSum))
 
 
