#!/usr/bin/python3
'''Pascal's Triangle module'''


def pascal_triangle(n):
    '''returns list of lists of integers represent Pascal’s triangle of n'''
    new_list = []
    prev_list = []
    res_list = []
    for row in range(n):
        new_list = []
        new_list.append(1)
        for i in range(len(prev_list)):
            if i < len(prev_list) - 1:
                new_list.append(prev_list[i] + prev_list[i + 1])
        if row != 0:
            new_list.append(1)
        prev_list = new_list
        res_list.append(prev_list)
    return res_list
