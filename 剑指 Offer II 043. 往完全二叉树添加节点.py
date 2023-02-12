# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 21:24 
# ide： PyCharm
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.c = collections.deque([root])
        while 1:
            p = self.c[0]
            if p.left and p.right:
                self.c.append(p.left)
                self.c.append(p.right)
                self.c.popleft()
            elif p.left:
                self.c.append(p.left)
                break
            elif p.right:
                self.c.append(p.right)
            else:
                break

    def insert(self, v: int) -> int:
        p = self.c[0]
        node = TreeNode(v)
        if not p.left:
            p.left = node
        else:
            p.right = node
            self.c.popleft()
        self.c.append(node)
        return p.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
# leetcode submit region end(Prohibit modification and deletion)
obj = CBTInserter(TreeNode(1))

