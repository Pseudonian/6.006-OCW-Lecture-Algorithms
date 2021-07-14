# -*- coding: utf-8 -*-
import math
import doctest
"""
OCW 6.006 Lecture 2 Code Writeup
Created on Wed Jul 14 08:42:30 2021

@author: Kevin Bunn
"""

#Lecture 2: Python Cost Model, Documentation Distance

#We will be implementing the document distance model in lecture.

def doc_distance(D1, D2):
    """
    Inputs:
        D1, D2 are both documents (strings of words)
    
    Output:
        A metric of how different the two documents are.

    The algorithm we will be implementing does the following in order:
        1) Splits documents 1, 2 into words.
        2) Compute Word Frequencies of documents 1, 2
        3) Compute dot product of words if applicable.
    
    >>> x = "dog dog dog dog dog"
    >>> y = "dog dog dog dog dog"
    >>> doc_distance(x, y)
    0.0
    """
    
    #Part 1: split D1, D2 into words list.
    d1_list = D1.split() #Linear Time O(n)
    d2_list = D2.split()
    
    #Part 2: Creates word dictionary counts.
    def freq_count(arr): #Linear Time O(n)
        count = {}
        for word in arr:
            if word in count:
                count[word] += 1
            else: #initialize key in dictionary
                count[word] = 1
    
        return count
    
    count1 = freq_count(d1_list)
    count2 = freq_count(d2_list)

    #Part 3: Compute the inner product and normalization factor.
    def dot_product(dict1, dict2): #Linear Time O(n)
        dot_product = 0
        for word in dict1.keys():
            if word in dict2.keys():
                #We only need to check one-way because word in d1 and d2 implies
                #the word is in d2 and d1.
                dot_product += dict1[word] * dict2[word]
        return dot_product
    
    dot = dot_product(count1, count2)
    #The magnitude of a vector is the dot product of itself.
    normal = (dot_product(count1, count1) * dot_product(count2, count2))**0.5
    
    #Part 5: return arccos of resulting angle measure.
    return math.acos(dot/normal) #O(1) operation

if __name__ == '__main__':
    doctest.testmod()