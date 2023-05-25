# binary search algorithm 

#naive search vs binary search
#naive: scan entire list, ask if equal to target -- iteration 

import random
import time


def naive_search(l, target):
    #l can be [1,3,5,10]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
    

#binary search using divide and conquer 

def binary_search(l, target, low=None, high=None):
    #low and high are indices 
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
        #highest possible we can check 

    if high<low:
        return -1

    #eg: l = [1,3,5,10,12] 
    midpoint = (low+high) // 2 #low is 0,  high is 4 -> midpt is 2

    if l[midpoint]==target:
        return midpoint
     
    elif target<l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    #recursion 

    else: 
        #target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
