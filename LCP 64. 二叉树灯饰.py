# -*- coding: utf-8 -*-
# 「力扣嘉年华」的中心广场放置了一个巨型的二叉树形状的装饰树。每个节点上均有一盏灯和三个开关。节点值为 `0` 表示灯处于「关闭」状态，节点值为 `1` 表示
# 灯处于「开启」状态。每个节点上的三个开关各自功能如下：
# - 开关 `1`：切换当前节点的灯的状态；
# - 开关 `2`：切换 **以当前节点为根** 的子树中，所有节点上的灯的状态，；
# - 开关 `3`：切换 **当前节点及其左右子节点**（若存在的话） 上的灯的状态；
#
# 给定该装饰的初始状态 `root`，请返回最少需要操作多少次开关，可以关闭所有节点的灯。
#
# **示例 1：**
#
# > 输入：`root = [1,1,0,null,null,null,1]`
# >
# > 输出：`2`
# >
# > 解释：以下是最佳的方案之一，如图所示
# > ![b71b95bf405e3b223e00b2820a062ba4.gif](https://pic.leetcode-cn.com/16293570
# 30-GSbzpY-b71b95bf405e3b223e00b2820a062ba4.gif)
#
# **示例 2：**
#
# > 输入：`root = [1,1,1,1,null,null,1]`
# >
# > 输出：`1`
# >
# > 解释：以下是最佳的方案，如图所示
# > ![a4091b6448a0089b4d9e8f0390ff9ac6.gif](https://pic.leetcode-cn.com/16293569
# 50-HZsKZC-a4091b6448a0089b4d9e8f0390ff9ac6.gif)
#
# **示例 3：**
#
# > 输入：`root = [0,null,0]`
# >
# > 输出：`0`
# >
# > 解释：无需操作开关，当前所有节点上的灯均已关闭
#
# **提示：**
# - `1 <= 节点个数 <= 10^5`
# - `0 <= Node.val <= 1`
#
#  Related Topics 树 深度优先搜索 动态规划 二叉树
#  👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        @lru_cache(None)
        def dfs(cur_node, switch2, switch3):
            if not cur_node:
                return 0
            if (cur_node.val == 1) == (switch2 == switch3):  # switch2不相同说明开关二三会切换当前灯，否则不会
                res1 = dfs(cur_node.left, switch2, 0) + dfs(cur_node.right, switch2, 0) + 1
                res2 = dfs(cur_node.left, switch2 ^ 1, 0) + dfs(cur_node.right, switch2 ^ 1, 0) + 1
                res3 = dfs(cur_node.left, switch2, 1) + dfs(cur_node.right, switch2, 1) + 1
                res123 = dfs(cur_node.left, switch2 ^ 1, 1) + dfs(cur_node.right, switch2 ^ 1, 1) + 3
                return min(res1, res2, res3, res123)
            else:
                res0 = dfs(cur_node.left, switch2, 0) + dfs(cur_node.right, switch2, 0)
                res13 = dfs(cur_node.left, switch2, 1) + dfs(cur_node.right, switch2, 1) + 2
                res12 = dfs(cur_node.left, switch2 ^ 1, 0) + dfs(cur_node.right, switch2 ^ 1, 0) + 2
                res23 = dfs(cur_node.left, switch2 ^ 1, 1) + dfs(cur_node.right, switch2 ^ 1, 1) + 2
                return min(res0, res13, res12, res23)
        return dfs(root, 0, 0)
# leetcode submit region end(Prohibit modification and deletion)
