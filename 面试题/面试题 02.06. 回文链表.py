#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编写一个函数，检查输入的链表是否是回文的。
#
#
#
#  示例 1：
#
#  输入： 1->2
# 输出： false
#
#
#  示例 2：
#
#  输入： 1->2->2->1
# 输出： true
#
#
#
#
#  进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#  Related Topics 栈 递归 链表 双指针
#  👍 75 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针求中点，偶数为左中位数
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse_node(node: ListNode):
            pre = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        def half_node(node: ListNode):
            fast = node
            slow = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        if not head:
            return True
        first = half_node(head)
        second = reverse_node(first.next)
        h1, h2 = head, second
        res = True
        while h1 and h2:
            if h1.val != h2.val:
                res = False
                break
            h1 = h1.next
            h2 = h2.next
        new_second = reverse_node(second)
        first.next = new_second
        return res
from leetcode.trick.listnode.L import stringToListNode
a=stringToListNode('[1,2,2,1]')
Solution().isPalindrome(a)