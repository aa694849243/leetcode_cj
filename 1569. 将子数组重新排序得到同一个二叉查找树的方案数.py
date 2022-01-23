#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉查找树（BST）。请你统计将 nums 重
# 新排序后，统计满足如下条件的方案数：重排后得到的二叉查找树与 nums 原本数字顺序得到的二叉查找树相同。
#
#  比方说，给你 nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组 [2,3,1] 也能得到相同的 BST，但 [3
# ,2,1] 会得到一棵不同的 BST 。
#
#  请你返回重排 nums 后，与原数组 nums 得到相同二叉查找树的方案数。
#
#  由于答案可能会很大，请将结果对 10^9 + 7 取余数。
#
#
#
#  示例 1：
#
#
#
#  输入：nums = [2,1,3]
# 输出：1
# 解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。
#
#
#  示例 2：
#
#
#
#  输入：nums = [3,4,5,1,2]
# 输出：5
# 解释：下面 5 个数组会得到相同的 BST：
# [3,1,2,4,5]
# [3,1,4,2,5]
# [3,1,4,5,2]
# [3,4,1,2,5]
# [3,4,1,5,2]
#
#
#  示例 3：
#
#
#
#  输入：nums = [1,2,3]
# 输出：0
# 解释：没有别的排列顺序能得到相同的 BST 。
#
#
#  示例 4：
#
#
#
#  输入：nums = [3,1,2,5,4,6]
# 输出：19
#
#
#  示例 5：
#
#  输入：nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
# 输出：216212978
# 解释：得到相同 BST 的方案数是 3216212999。将它对 10^9 + 7 取余后得到 216212978。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 1000
#  1 <= nums[i] <= nums.length
#  nums 中所有数 互不相同 。
#
#  Related Topics 树 并查集 二叉搜索树 记忆化搜索 数组 数学 分治 动态规划 二叉树 组合数学
#  👍 36 👎 0

# 费马小定理题目二刷再看
# https://leetcode-cn.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/solution/jiang-zi-shu-zu-zhong-xin-pai-xu-de-dao-tong-yi-2/
class TNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.ans = 0
        self.size = 1


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        c = [[0] * n for _ in range(n)]  # 组合公式
        c[0][0] = 1
        for i in range(1, n):
            c[i][0] = 1
            for j in range(1, n):
                c[i][j] = (c[i - 1][j - 1] + c[i-1][j]) % mod
        root = TNode(nums[0])

        def insert(i):  # 每insert 1 个数，size+=1
            cur = root
            while 1:
                cur.size += 1
                if cur.val > i:
                    if not cur.left:
                        cur.left = TNode(i)
                        return
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = TNode(i)
                        return
                    cur = cur.right

        if len(nums) == 1:
            return 0
        for i in nums[1:]:
            insert(i)

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            lsize = node.left.size if node.left else 0
            rsize = node.right.size if node.right else 0
            lans = node.left.ans if node.left else 1
            rans = node.right.ans if node.right else 1
            node.ans = c[lsize + rsize][lsize] * lans * rans  # 小规模子问题
            return node.ans  # 如果左右子树都为0的话node.ans=1

        dfs(root)
        return (root.ans - 1) % mod
Solution().numOfWays([3,4,5,1,2])