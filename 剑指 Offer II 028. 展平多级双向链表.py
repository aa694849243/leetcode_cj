# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-07 21:44 
# ide： PyCharm
class Solution:
    def flatten(self, head: 'Node') -> 'None':
        def dfs(node) -> ('Node', 'Node'):
            if not node.next and not node.child:
                return node, node
            elif node.next and node.child:
                nxt, tail = dfs(node.next)
                c_h, c_t = dfs(node.child)
                node.next = c_h
                c_h.prev = node
                c_t.next = nxt
                nxt.prev = c_t
                node.child = None
                return node, tail
            elif node.next and not node.child:
                return node, dfs(node.next)[1]
            elif not node.next and node.child:
                c_h, c_t = dfs(node.child)
                node.next = c_h
                c_h.prev = node
                node.child = None
                return node, c_t

        if not head:
            return head
        return dfs(head)[0]


# leetcode submit region end(Prohibit modification and deletion)
node1 = Node(1, None, None, None)
node2 = Node(2, None, None, None)
node3 = Node(3, None, None, None)
node1.child = node2
node2.child = node3
# node2.prev = node1
# node1.next = node2
# node1.child = node3

print(
    Solution().flatten(
        node1
    ))

