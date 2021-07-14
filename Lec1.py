import math
import doctest
import random
# -*- coding: utf-8 -*-
"""
OCW 6.006 Lecture 1 Code Writeup

Created on Tue Jul 13 19:15:56 2021

@author: Kevin Bunn
"""
#Hello! This is a 40 something lecture series on the OCW website @MIT.
#lectures tend to discuss particular problems and algorithms to solve them.

#I will be documenting my particular implementations to these problems, in order to
#both get better at python, but also to improve my implementations on algorithms
#to prepare for interviews. If you'd like to follow along, the playlist is somewhere
#on youtube to be watched freely.

#Part 1: 1 dimensional peak finding.
#Goal: O(log(n)) time. We will be using Binary Search divide&conquer.

def one_dim_peak(arr, pointer = 0):
    """
    Find a 'peak' in a 1d array, giving value and position. given a list [a0, a1, ... , an-1] a peak
    is defined where for ai, ai-1 <= ai and ai+1 <= ai.
    >>> one_dim_peak([1,2,3,4,5,2,1])
    (5, 4)
    """
    #Base case [We consider singletons to have a peak]
    if len(arr) == 1:
        return (arr[0], pointer)
    
    #Initialize our midpoint. I decided to use a left-bias in my binary search algorithm.
    mid = math.floor((len(arr) - 1)/2)
    left = mid > 0 #Prevent out-of-range error for edge cases
    
    #Recursive case
    if arr[mid - 1] > arr[mid] and left: 
        #Left side of our midpoint has a peak
        return one_dim_peak(arr[0:mid], pointer)
    elif arr[mid + 1] > arr[mid]:
        #Right side of midpoint has a peak
        return one_dim_peak(arr[mid+1:len(arr)], pointer + mid + 1)
    else:
        #We've obtained a peak, so return its value and index.
        return (arr[mid], mid)

#Part 2: 2 dimensional peak finding.
#Goal: O(nlog(n)) time. Binary search again.

def two_dim_peak(arr, row=0):
    """
    Find a 'peak' in a 2d array. given [[a00, ... , a0n], [a10, ... , a1n], ... , [am0, ..., amn]]
    a peak is one such that any of its horizontal or vertical neighbors are less than or equal to that value.
    >>> two_dim_peak([[1,2,3],[4,5,6],[7,8,9]])
    (9, (2, 2))
    """
    #Base case [We consider single rows to have a peak]
    if len(arr) == 1:
        row_val, row_pos = one_dim_peak(arr[0])
        return (row_val, (row, row_pos))
    
    #Initialize midpoint and check for row being valid.
    mid = math.floor((len(arr) - 1)/2)
    up = mid > 0
    
    #Obtain the index j of the peak of mid row.
    row_val, row_pos = one_dim_peak(arr[mid])
    
    #Recursive case
    if arr[mid - 1][row_pos] > arr[mid][row_pos] and up:
        #Rows above mid contain peak
        return two_dim_peak(arr[0:mid], row)
    elif arr[mid + 1][row_pos] > arr[mid][row_pos]:
        #Rows below mid contain peak
        return two_dim_peak(arr[mid+1:len(arr)], row + mid + 1)
    else:
        #We've obtained a peak, so we return value and coordinates.
        return (arr[mid][row_pos], (mid, row_pos))
    
if __name__ == '__main__':
    doctest.testmod()
    #arr2d = []
    #for i in range(12):
    #    arr2d.append(random.sample(range(10, 40), 12))
    
    #print(arr2d)
    #print(two_dim_peak(arr2d))
    
    #arr = random.sample(range(2**10), 1000)
    #print(arr)
    #print(one_dim_peak(arr)) #Note: if there's a way to visualize this, the reader can try to implement that.