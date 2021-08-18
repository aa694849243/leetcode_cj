#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定两个用链表表示的整数，每个节点包含一个数位。
#
#  这些数位是反向存放的，也就是个位排在链表首部。
#
#  编写函数对这两个整数求和，并用链表形式返回结果。
#
#
#
#  示例：
#
#  输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912
#
#
#  进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?
#
#  示例：
#
#  输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
# 输出：9 -> 1 -> 2，即912
#
#  Related Topics 递归 链表 数学
#  👍 86 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        H = ListNode(-1)
        head = H
        carry = 0
        while l1 and l2:
            carry, val = divmod(int(l1.val) + int(l2.val) + carry, 10)
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            carry, val = divmod(l1.val + carry, 10)
            if not carry:
                l1.val = val
                head.next = l1
                break
            l1=l1.next
            head.next = ListNode(val)
            head = head.next
        while l2:
            carry, val = divmod(int(l2.val) + carry, 10)
            if not carry:
                l2.val = val
                head.next = l2
                break
            l2=l2.next
            head.next = ListNode(val)
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return H.next


from leetcode.trick.listnode.L import stringToListNode

l1 = stringToListNode('[1]')
l2 = stringToListNode('[9,9]')
Solution().addTwoNumbers(l1, l2)
