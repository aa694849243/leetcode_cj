# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-07 22:05 
# ide： PyCharm

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        H = head
        head = head.next
        i_node = Node(insertVal)
        while 1:
            if head.val <= insertVal <= head.next.val or (
                    head.next.val < head.val and (insertVal <= head.next.val or insertVal >= head.val)) or head == H:
                head.next, i_node.next = i_node, head.next
                break

            head = head.next
        return H


# leetcode submit region end(Prohibit modification and deletion)
node1 = Node(3)
node2 = Node(3)
node3 = Node(5)
node1.next = node
print(
    Solution().insert(
        Node(1), 0
    )
)
