#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    size_1 = len(xs) 
    size_2 = len(ys) 
    
    res = [] 
    i, j = 0, 0
    
    while i < size_1 and j < size_2: 
        if cmp(xs[i], ys[j]) == -1: 
            res.append(xs[i]) 
            i += 1
        else: 
            res.append(ys[j]) 
            j += 1
    
    res = res + xs[i:] + ys[j:]
    return res



def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    if len(xs) == 0:
        return xs
    if len(xs) == 1:
        return xs
    else:
        mid = len(xs)//2
        leftlist = xs[:mid]
        rightlist = xs[mid:]
        l = merge_sorted(leftlist, cmp=cmp)
        r = merge_sorted(rightlist, cmp=cmp)
        return _merged(l,r)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''
    if len(xs) == 1:
        return xs
    else:
        quickSortHelper(xs,0,len(xs)-1)
        return xs

def quickSortHelper(xs,first,last):
    if first<last:
        splitpoint = partition(xs,first,last)
        quickSortHelper(xs,first,splitpoint-1)
        quickSortHelper(xs,splitpoint+1,last)


def partition(xs,first,last, cmp = cmp_standard):
    pivotvalue = xs[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while cmp(leftmark,rightmark) <= 0 and cmp(xs[leftmark],pivotvalue) <= 0:
            leftmark = leftmark + 1
        while cmp(xs[rightmark], pivotvalue) >= 0 and cmp(rightmark, leftmark) >= 0:
            rightmark = rightmark -1
        if cmp(rightmark, leftmark) == -1:
            done = True
        else:
            temp = xs[leftmark]
            xs[leftmark] = xs[rightmark]
            xs[rightmark] = temp
    temp = xs[first]
    xs[first] = xs[rightmark]
    xs[rightmark] = temp
    return xs

