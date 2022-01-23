#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。
#
#  对于每个整数：
#
#
#  百位上的数字表示这个节点的深度 D，1 <= D <= 4。
#  十位上的数字表示这个节点在当前层所在的位置 P， 1 <= P <= 8。位置编号与一棵满二叉树的位置编号相同。
#  个位上的数字表示这个节点的权值 V，0 <= V <= 9。
#
#
#  给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，请你返回从根到所有叶子结点的路径之和。
#
#
#
#  示例 1：
#
#
# 输入: [113, 215, 221]
# 输出: 12
# 解释:
# 这棵树形状如下:
#     3
#    / \
#   5   1
#
# 路径和 = (3 + 5) + (3 + 1) = 12.
#
#
#  示例 2：
#
#
# 输入: [113, 221]
# 输出: 4
# 解释:
# 这棵树形状如下:
#     3
#      \
#       1
#
# 路径和 = (3 + 1) = 4.
#
#
#
#  Related Topics 树 深度优先搜索 数组 二叉树
#  👍 41 👎 0


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        g = collections.defaultdict(dict)
        for num in nums:
            w = str(num)
            g[int(w[0])][int(w[1])] = int(w[2])
        self.res = 0

        def rec(presum, curlevel, curp):
            if curlevel+1 in g and 2*curp in g[curlevel+1] or 2*curp-1 in g[curlevel+1]:
                if 2 * curp in g[curlevel + 1]:
                    rec(presum + g[curlevel][curp], curlevel + 1, 2 * curp)
                if 2 * curp - 1 in g[curlevel + 1]:
                    rec(presum + g[curlevel][curp], curlevel + 1, 2 * curp - 1)
            else:
                self.res += presum + g[curlevel][curp]

        rec(0, 1, 1)
        return self.res
