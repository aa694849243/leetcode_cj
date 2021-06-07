# -*- coding: utf-8 -*-
from typing import List


# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
#
#  如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
#
#  而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
#
#
#
#  给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
#
#
#
#  示例 1：
#
#  输入：label = 14
# 输出：[1,3,4,14]
#
#
#  示例 2：
#
#  输入：label = 26
# 输出：[1,2,6,10,26]
#
#
#
#
#  提示：
#
#
#  1 <= label <= 10^6
#
#  Related Topics 树 数学
#  👍 71 👎 0

# https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/solution/jian-dan-yi-dong-de-gong-shi-shi-jian-guo-100-by-a/
# 因为隔层翻转，所以每一个节点的父节点都为原父节点的对称点
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        self.ans = []

        def dfs(n, level):
            if n == 1:
                self.ans.append(n)
                return self.ans
            parent = 3 * 2 ** (level - 1) - 1 - n // 2
            self.ans.append(n)
            return dfs(parent, level - 1)

        carry = 1
        level = 0
        while carry <= label:
            carry <<= 1
            level += 1
        return dfs(label,level-1)[::-1]
Solution().pathInZigZagTree(14)