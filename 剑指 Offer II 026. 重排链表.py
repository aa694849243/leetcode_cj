# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-07 0:17 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l1 = head
        mid = self.find_mid(head)
        l2 = mid.next
        mid.next = None
        l2 = self.reversed_list(l2)
        self.merge_two_list(l1, l2)
        return

    def reversed_list(self, head: ListNode) -> ListNode:
        """
        反转链表
        """
        cur = head
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def find_mid(self, head: ListNode) -> ListNode:
        """
        找到链表的中间节点
        """
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_two_list(self, l1, l2):
        while l1 and l2:
            n1, n2 = l1.next, l2.next
            l1.next, l2.next = l2, n1
            l1, l2 = n1, n2


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().reorderList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    ))

