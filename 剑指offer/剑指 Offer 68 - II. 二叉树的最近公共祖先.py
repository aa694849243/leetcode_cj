#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 哈希表法可看c++
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def dfs(node):
            if not node:
                return False
            f = False
            if node.val == p.val or node.val == q.val:
                f = True
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r and not self.ans:
                self.ans = node
            elif f and (l or r) and not self.ans:
                self.ans = node
            return f or l or r

        dfs(root)
        return self.ans
