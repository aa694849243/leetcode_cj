# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-05-05 23:29 
# ide： PyCharm
import heapq
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        t = [root]
        hq = []
        res = -1
        while 1:
            tree = []
            tmp = 0
            for node in t:
                tmp += node.val
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            heapq.heappush(hq, tmp)
            if len(hq) > k:
                heapq.heappop(hq)
            if not tree:
                break
            t = tree
        if len(hq) == k:
            res = hq[0]
        return res

