# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 23:48 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        p = head
        while p != slow:
            p, slow = p.next, slow.next
        return p
# leetcode submit region end(Prohibit modification and deletion)

