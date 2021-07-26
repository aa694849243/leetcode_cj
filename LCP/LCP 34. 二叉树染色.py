# -*- coding: utf-8 -*-
# 小扣有一个根结点为 `root` 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 `val` 价值。小扣出于美观考虑
# ，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 `k` 个，求所有染成蓝色的结点价值总和最大是多少？
#
#
# **示例 1：**
# > 输入：`root = [5,2,3,4], k = 2`
# >
# > 输出：`12`
# >
# > 解释：`结点 5、3、4 染成蓝色，获得最大的价值 5+3+4=12`
# ![image.png](https://pic.leetcode-cn.com/1616126267-BqaCRj-image.png)
#
#
# **示例 2：**
# > 输入：`root = [4,1,3,9,null,null,2], k = 2`
# >
# > 输出：`16`
# >
# > 解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16
# ![image.png](https://pic.leetcode-cn.com/1616126301-gJbhba-image.png)
#
#
#
# **提示：**
# + `1 <= k <= 10`
# + `1 <= val <= 10000`
# + `1 <= 结点数量 <= 10000`
#  Related Topics 树 动态规划 二叉树
#  👍 21 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            dp = [0] * (k + 1)  # dp[i]代表该节点连续染色i个数量的最大值
            if not node:
                return dp
            l, r = dfs(node.left), dfs(node.right)
            dp[0] = max(l) + max(r)  # node节点不染色
            for i in range(1, k + 1): #染色后，dp[i]代表该节点染色，且连续数量为i的最大值
                dp[i] = max(l[p] + r[i - p - 1] for p in range(i)) + node.val #p代表左子树连续染色的数量，i-p-1代表右子树连续染色数量
            return dp

        return max(dfs(root))
