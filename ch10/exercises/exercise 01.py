# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:14:46 2018

@author: Pshypher
"""
def sum_lists_a(list1,list2):
    """Element-by-element sums of two lists of 9 items."""
    sums_list = []
   
    for index in range(len(list1)):
        sums_list.append(list1[index]+list2[index])
    return sums_list


def sum_lists_b(list1,list2):
    """Element-by-element sums of two lists of 9 items."""
    sums_list = []
    # the shorter of both list length is used to iterate through and sum the
    # integers in both lists
    list_length = len(list1) if len(list1) < len(list2) else len(list2)
    for index in range(list_length):
        sums_list.append(list1[index]+list2[index])
    return sums_list

def sum_lists_c(list1,list2):
    """Element-by-element sums of two lists of 9 items."""
    return [list1[index]+list2[index] for index in range(9)]