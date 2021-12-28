#!/usr/bin/env python
# -*- coding: utf-8 -*-
# nishulong n00299121对所有人说说： 07:50 PM
# 题目描述：
# 给定一个由正整数组成的数列，如果能剔除其中一个元素，使得数列有序，则返回这个元素，否则返回-1
# 所谓有序，即要么递增要么递减（不需要一定是严格递增或严格递减，如 1 2 2 3 满足递增有序）
# 注意：
# 如果给定的数列已经是有序的，则直接返回 -1
# 如果可行方案有多个，则输出被剔除元素值最小的那个
# 接口定义：
# def func(input_list):
#     # TODO
# return -1
# 测试用例：
# 用例1：
# 输入：[1, 2, 2, 3]
# 输出：-1
# 用例2：
# 输入：[2, 2, 1, 3]
# 输出：1
# 用例3：
# 输入：[1, 3, 2, 6, 7]
# 输出：2
def cal(lst):
    if lst == sorted(lst):
        return -1
    if lst == sorted(lst)[::-1]:
        return -1
    lst2 = sorted(lst)
    for i, num in enumerate(lst2):
        if num != lst[i]:
            nlst2 = lst2[:i] + lst2[i + 1:]
            index = lst.index(num)
            nlst = lst[:index] + lst[index + 1:]
            if nlst2 == nlst:
                return num

    lst3 = sorted(lst)[::-1]
    for i, num in enumerate(lst3):
        if num != lst[i]:
            nlst3 = lst3[:i] + lst3[i + 1:]
            index = lst.index(num)
            nlst = lst[:index] + lst[index + 1:]
            if nlst3 == nlst:
                return num
    return -1


lst = [1,3,3,2,2,6,7]
print(cal(lst))
