# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        T = [root]
        ans = 0
        while 1:
            tree = []
            for node in T:
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            a = sorted(range(len(tree)), key=lambda x: tree[x].val)
            ans += len(a)
            visted = [False] * len(a)
            for v in a:
                if visted[v]:
                    continue
                while not visted[v]:
                    visted[v] = True
                    v = a[v]
                ans -= 1  # 成一个环减一次
            if not tree:
                break
            T = tree
        return ans
# leetcode submit region end(Prohibit modification and deletion)
