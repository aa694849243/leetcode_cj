# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 21:32 
# ide： PyCharm
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        T=[root]
        ans=[]
        while 1:
            tree=[]
            for node in T:
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            ans.append(T[-1].val)
            if not tree:
                break
            T=tree
        return ans
# leetcode submit region end(Prohibit modification and deletion)

