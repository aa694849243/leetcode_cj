#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


def cal(lst, target):
    m = collections.Counter(lst)
    for i in range(len(lst)):
        if target - lst[i] in m:
            if target - lst[i] == lst[i]:
                if m[lst[i]] > 1:
                    a = lst[i + 1:].index(lst[i])
                    res=[i,i+1+a]
                    return [i, i + 1 + a]
            else:
                a = lst[i + 1:].index(target - lst[i])
                res=[i,i+1+a]
                return [i, i + 1 + a]
    return [-1,-1]

cal([1,2,3,4,1,1,2,4],6)