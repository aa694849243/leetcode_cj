# -*- coding: utf-8 -*-
import collections


def tes():
    dcc = []
    stack = []
    dfn = [0] * 100
    low = [0] * 100
    g = collections.defaultdict(set)

    cuts = set()
    timestamp = 1

    def tarjan3(cur):
        nonlocal timestamp
        dfn[cur] = low[cur] = timestamp
        timestamp += 1
        child_num = 0
        stack.append(cur)
        for child in g[cur]:
            if dfn[child] == 0:
                tarjan3(child)
                low[cur] = min(low[cur], low[child])
                if low[child] >= dfn[cur]:
                    child_num += 1
                    if cur != root or child_num > 1:
                        cuts.add(cur)
                    dcc.append([])
                    t = stack.pop()
                    dcc[-1].append(t)
                    while t != child:
                        t = stack.pop()
                        dcc[-1].append(t)
                    dcc[-1].append(cur)
            else:
                low[cur] = min(low[cur], dfn[child])
        if cur == root and child_num == 0:
            dcc.append([cur])

    def add(x, y):
        g[x].add(y)
        g[y].add(x)

    add(1, 2)
    add(1, 3)
    # add(2, 3)
    root = 1
    tarjan3(1)
    print(cuts)
    print(dcc)
tes()