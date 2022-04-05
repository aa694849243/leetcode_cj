#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Seg:
    def __init__(self, l=-1, r=-1):
        self.left = l
        self.right = r

    def __lt__(self, other):
        return self.right < other.right if self.right != other.right else self.left > other.left


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        Segs = [Seg() for _ in range(26)]
        for i, ch in enumerate(s):
            index = ord(ch) - 97
            seg = Segs[index]
            if seg.left == -1:
                seg.left = seg.right = i
            else:
                seg.right = i
        for seg in Segs:
            if seg.left == -1:
                continue
            j = seg.left
            while j < seg.right:
                index = ord(s[j]) - 97
                if seg.left <= Segs[index].left and seg.right >= Segs[index].right:
                    j += 1
                    continue
                else:
                    seg.left = min(seg.left, Segs[index].left)
                    seg.right = max(seg.right, Segs[index].right)
                    j = seg.left
                    j += 1
        Segs.sort()
        res = []
        end = -1
        for seg in Segs:
            if seg.left == -1:
                continue
            else:
                l, r = seg.left, seg.right
                if end == -1:
                    res.append(s[l:r + 1])
                    end = r
                elif l > end:
                    res.append(s[l:r + 1])
                    end = r
        return res


Solution().maxNumOfSubstrings("adefaddaccc")
