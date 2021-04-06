'''
我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。

 

示例 1：



输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
示例 2：



输入："1-2--3---4-5--6---7"
输出：[1,2,5,3,null,6,null,4,null,7]
示例 3：



输入："1-401--349---90--88"
输出：[1,401,null,349,88,90]
 

提示：

原始树中的节点数介于 1 和 1000 之间。
每个节点的值介于 1 和 10 ^ 9 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# stack长度作层数
# 官方题解 https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/cong-xian-xu-bian-li-huan-yuan-er-cha-shu-by-leetc/
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        stack = []
        while i < len(S):
            st = ''
            level = 0
            while S[i] == '-':
                level += 1
                i += 1
            while i < len(S) and S[i] != '-':
                st += S[i]
                i += 1
            node = TreeNode(int(st))
            if not stack:
                pass
            elif level == len(stack):
                stack[-1].left = node
            elif level == len(stack) - 1:
                stack.pop()
                stack[-1].right = node
            else:
                stack = stack[:level]
                stack[-1].right = node
            stack.append(node)
        return stack[0]


Solution().recoverFromPreorder("1-401--349---90--88")
