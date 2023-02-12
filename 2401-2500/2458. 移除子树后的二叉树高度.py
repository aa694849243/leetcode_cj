# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level = collections.defaultdict(int)
        m = {}

        def dfs(node):
            m[node.val] = node
            if not node.left and not node.right:
                return 0
            level_left = level_right = 0
            if node.left:
                level_left = dfs(node.left)
            if node.right:
                level_right = dfs(node.right)
            level[node.val] = max(level_left, level_right) + 1
            return level[node.val]

        dfs(root)
        res = {}
        step = 1
        T = [root]
        while 1:
            tree = []
            h = []
            for node in T:
                if node.left:
                    tree.append(node.left)
                    h.append(level[node.left.val])
                if node.right:
                    tree.append(node.right)
                    h.append(level[node.right.val])
            if not tree:
                break
            if len(tree) != 1:
                nd, st = sorted(h)[-2:]
            else:
                nd, st = -1, h[0]
            if st != nd:
                p = h.index(st)
                res[tree[p].val] = nd + step
            step += 1
            T = tree

        ans = [level[root.val]] * len(queries)
        for i, val in enumerate(queries):
            if val in res:
                ans[i] = res[val]
        return ans


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


root = stringToTreeNode('[1,null,5,3,null,2,4]')
queries = [3]
print(Solution().treeQueries(root, queries))
