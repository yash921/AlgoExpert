#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:07:54 2020

@author: yash
"""

# Solution 1
# Upper Bound: O(n^2*n) time | O(n*n!) space
## Roughly: O(n*n!)  time | O(n*n!) space
def getPermutation(array):
    permutations = []
    permutationHelper(array, [], permutations)
    return permutations

def permutationHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)

#Solution 1
## O(n*n!)  time | O(n*n!) space
def getPermutation(array):
    permutations = []
    permutationhelper(0, array, permutations)
    return permutations

def permutationhelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array,i,j)
            permutationhelper(i+1, array, permutations)
            swap(array,i,j)
            
def swap(array,i,j):
    array[i], array[j] = array[j], array[i]
