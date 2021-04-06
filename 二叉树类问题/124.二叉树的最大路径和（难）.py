'''
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution:
    def __init__(self):
        self.maxscore = float('-inf')
        self.s = {}

    def maxPathSum(self, root: TreeNode) -> int:
        def gainscore(Node):
            if not Node:
                return float('-inf')
            elif not (Node.left or Node.right):
                self.s[Node] = Node.val
                return self.s[Node]
            elif not Node.left:
                self.s[Node] = Node.val + max(gainscore(Node.right), 0)
                return self.s[Node]
            elif not Node.right:
                self.s[Node] = Node.val + max(gainscore(Node.left), 0)
                return self.s[Node]
            else:
                self.s[Node] = Node.val + max(gainscore(Node.left), gainscore(Node.right), 0)
                return self.s[Node]

        def dfs(Node):
            if not Node:
                return
            elif not Node.left:
                self.maxscore = max(self.maxscore, Node.val + max(self.s.get(Node.right, 0), 0))
                dfs(Node.right)
            elif not Node.right:
                self.maxscore = max(self.maxscore, Node.val + max(self.s.get(Node.left, 0), 0))
                dfs(Node.left)
            else:
                self.maxscore = max(self.maxscore,
                                    Node.val + max(self.s.get(Node.right, 0), 0) + max(
                                        self.s.get(Node.left, 0), 0))

                dfs(Node.left)
                dfs(Node.right)
        gainscore(root)
        dfs(root)
        return self.maxscore

#递归
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / binary - tree - maximum - path - sum / solution / er - cha - shu - zhong - de - zui - da - lu - jing - he - by - leetcode - /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

root = stringToTreeNode('[-2,1]')
Solution().maxPathSum(root)
