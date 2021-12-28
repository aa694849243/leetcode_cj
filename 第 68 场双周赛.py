#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 5946. 句子中的最多单词数
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for w in sentences:
            res = max(res, len(w.split()))
        return res


# 5947. 从给定原材料中找到所有可以做出的菜
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = collections.defaultdict(set)
        n = len(recipes)
        indgrees = collections.defaultdict(int)
        for i, v in enumerate(recipes):
            for ingr in ingredients[i]:
                g[ingr].add(v)
                indgrees[v] += 1
        st = collections.deque(supplies)
        m = set(recipes)
        res = []
        while st:
            a = st.popleft()
            for nxt in g[a]:
                indgrees[nxt] -= 1
                if indgrees[nxt] == 0:
                    if nxt in m:
                        res.append(nxt)
                    st.append(nxt)
        return res


# 5948. 判断一个括号字符串是否有效
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        ops = collections.deque()
        stack = collections.deque()
        for i, op in enumerate(locked):
            if op == '0':
                ops.append(1)
            else:
                if s[i] == '(':
                    stack.append(('(', i))
                else:
                    if stack and stack[-1][0] == '(':
                        stack.pop()
                    else:
                        stack.append((')', i))
                ops.append(0)
        o = 0
        bal = 0
        for i in range(len(ops)):
            if ops[i] == 1:
                o += 1
                if bal > 0:
                    o -= 1
                    bal -= 1
            else:
                if not stack or stack[0][1] != i:
                    continue
                if stack[0][0] == ')':
                    o -= 1
                    if o < 0:
                        return False
                    stack.popleft()
                elif stack[0][0] == '(':
                    bal += 1
                    stack.popleft()
        return bal == 0 and o % 2 == 0


# 5949. 一个区间内所有数乘积的缩写
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        if left == right:
            c = 0
            while left % 10 == 0:
                c += 1
                left //= 10
            if len(str(left)) > 10:
                return str(left)[:5] + '...' + str(left[-5:]) + 'e' + str(c)
            else:
                return str(left) + 'e' + str(c)

        pre = 1
        c = 0
        flag = False
        for i in range(left, right + 1):
            pre *= i
            while i % 5 == 0:
                i //= 5
                c += 1
            while pre % 10 == 0:
                pre //= 10
            if len(str(pre)) > 10:
                flag = True
            if len(str(pre)) > 15:
                pre = int(str(pre)[:15])
        suf = 1
        for i in range(left, right + 1):
            suf *= i
            while suf % 10 == 0:
                suf //= 10
            if len(str(suf)) > 15:
                suf = int(str(suf)[-15:])
        if flag:
            return str(pre)[:5] + '...' + str(suf)[-5:] + 'e' + str(c)
        else:
            return str(pre) + 'e' + str(c)
