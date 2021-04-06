'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        prev = None
        while head:
            ne = head.next
            head.next = prev
            prev = head
            head = ne
        return prev

from leetcode.trick.listnode.L import stringToListNode
# 递归写法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rec(node1, node2):
            if not node2:
                return node1
            else:
                ne=node2.next
                node2.next = node1
                return rec(node2,ne)

        return rec(None, head)
a=stringToListNode('[1,2,3,4,5]')
Solution().reverseList(a)