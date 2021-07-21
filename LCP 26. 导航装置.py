# -*- coding: utf-8 -*-

# 小扣参加的秋日市集景区共有 $N$ 个景点，景点编号为 $1$~$N$。景点内设有 $N-1$ 条双向道路，使所有景点形成了一个二叉树结构，根结点记为 `r
# oot`，景点编号即为节点值。
#
# 由于秋日市集景区的结构特殊，游客很容易迷路，主办方决定在景区的若干个景点设置导航装置，按照所在景点编号升序排列后定义装置编号为 1 ~ M。导航装置向游客发
# 送数据，数据内容为列表 `[游客与装置 1 的相对距离,游客与装置 2 的相对距离,...,游客与装置 M 的相对距离]`。由于游客根据导航装置发送的信息来确认
# 位置，因此主办方需保证游客在每个景点接收的数据信息皆不相同。请返回主办方最少需要设置多少个导航装置。
#
# **示例 1：**
# >输入：`root = [1,2,null,3,4]`
# >
# >输出：`2`
# >
# >解释：在景点 1、3 或景点 1、4 或景点 3、4 设置导航装置。
# >
# >![image.png](https://pic.leetcode-cn.com/1597996812-tqrgwu-image.png){:height
# ="250px"}
#
#
#
# **示例 2：**
# >输入：`root = [1,2,3,4]`
# >
# >输出：`1`
# >
# >解释：在景点 3、4 设置导航装置皆可。
# >
# >![image.png](https://pic.leetcode-cn.com/1597996826-EUQRyz-image.png){:height
# ="200px"}
#
#
#
# **提示：**
# - `2 <= N <= 50000`
# - 二叉树的非空节点值为 `1~N` 的一个排列。
#  Related Topics 树 动态规划 二叉树
#  👍 8 👎 0


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode-cn.com/problems/hSRGyL/solution/tan-xin-suan-fa-zheng-ming-by-newhar/
class Solution:
    def navigation(self, root: TreeNode) -> int:
        self.ans = 0
        self.s = 1

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)  # 判断左右子树是不是三叉节点
            if node.left and node.right:  # 必须同时存在左右节点才考虑加导航器的问题，要不然相当于单链了，如果不加这个条件，末端节点也+1了
                if not l and not r:  # 只有左右子树都返回0时才+1，因为如果左右子树有一个是三叉节点的话，必定已经+1了，加上假设父节点有导航器，那么这个节点就不用加了
                    self.ans += 1
                self.s = not (l and r)  # self.s为最后计算的，也就是最近的三叉节点的左右子树状态，又由于是存在左右子树才能计算到self.s所以非三叉节点不会考虑
                return 1
            return l or r

        l, r = dfs(root.left), dfs(root.right)
        if not l or not r: #左右子树只有一棵是三叉节点
            self.ans+=self.s
        return self.ans

