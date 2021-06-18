# -*- coding: utf-8 -*-
from typing import List


# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
#
#
#  每个节点都有 0 个或是 2 个子节点。
#  数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
#  每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
#
#
#  在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
#
#
#
#  示例：
#
#  输入：arr = [6,2,4]
# 输出：32
# 解释：
# 有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。
#
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4
#
#
#
#  提示：
#
#
#  2 <= arr.length <= 40
#  1 <= arr[i] <= 15
#  答案保证是一个 32 位带符号整数，即小于 2^31。
#
#  Related Topics 栈 树 动态规划
#  👍 169 👎 0

# 1动态规划
# https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/dong-tai-gui-hua-dan-diao-zhan-python3-by-smoon1-2/
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf')] * n for _ in range(n)]
        maxval = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                maxval[i][j] = max(arr[i:j + 1])
        for i in range(n):  # 叶子节点不参与计算
            dp[i][i] = 0
        for l in range(1, n):
            for s in range(n - l):
                for k in range(s, s + l):
                    dp[s][s + l] = min(dp[s][s + l], dp[s][k] + dp[k + 1][s + l] + maxval[s][k] * maxval[k + 1][s + l])
        return dp[0][n - 1]


# 红笔记
# 寻找数组中某个数最近的大于这个数的位置
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:  # 找谷底元素最临近两个数
        stack = [float('inf')]
        res = 0
        for i, num in enumerate(arr):
            while stack[-1] <= num:
                a = stack.pop()
                res += a * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop()*stack[-1]
        return res


Solution().mctFromLeafValues([6, 2, 4])
