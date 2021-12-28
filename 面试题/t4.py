#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
import functools

while 1:
    try:
        ma = [[1,1],[2,2]]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []
        row,col=2,2


        def rec(r, c, lst):
            global res
            if (r, c) == (row - 1, col - 1):
                res = lst
                return
            else:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and ma[nr][nc] == 0:
                        rec(nr, nc, lst + [(nr, nc)])


        rec(0, 0, [])
        for ins in res:
            print(ins)
    except:
        break

