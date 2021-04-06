'''给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

 

示例 1：
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：

  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。

 

提示： 假设任意子树元素和均可以用 32 位有符号整数表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-frequent-subtree-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        import heapq
        import collections
        m = collections.defaultdict(int)

        def rec(node):
            if not node.left and not node.right:
                m[node.val] += 1
                return node.val
            elif not node.left:
                x = node.val + rec(node.right)
                m[x] += 1
                return x
            elif not node.right:
                x = node.val + rec(node.left)
                m[x] += 1
                return x
            else:
                x = node.val + rec(node.left) + rec(node.right)
                m[x] += 1
                return x
        if not root:
            return []
        rec(root)
        ans = []
        a = sorted(m.items(), reverse=True, key=lambda x: x[1])
        ans.append(a[0][0])
        for i in range(1,len(a)):
            if a[i][1]==a[i-1][1]:
                ans.append(a[i][0])
            else:
                break
        return ans
from leetcode.trick.treenode.T import stringToTreeNode
x=stringToTreeNode('[5,2,-3]')
Solution().findFrequentTreeSum(x)