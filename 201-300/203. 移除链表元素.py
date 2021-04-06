'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        H = ListNode(0)
        H.next = head
        prev = H
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return H.next
