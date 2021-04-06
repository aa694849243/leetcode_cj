'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

 

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from leetcode.trick.treenode.T import stringToTreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 卡特兰数 精妙递归
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)

                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n) if n else []


class Solution:
    def generateTrees(self, n):
        def generate_T(left, right):
            if left > right:
                return [None, ]
            ans = []
            for i in range(left, right + 1):
                left_trees = generate_T(left, i - 1)
                right_trees = generate_T(i + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        current_root = TreeNode(i)
                        current_root.left = l
                        current_root.right = r
                        ans.append(current_root)
            return ans

        return generate_T(1, n) if n else 0


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / unique - binary - search - trees - ii / solution / bu - tong - de - er - cha - sou - suo - shu - ii - by - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
Solution().generateTrees(3)
