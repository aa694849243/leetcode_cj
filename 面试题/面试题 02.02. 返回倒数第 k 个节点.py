#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
#
#  注意：本题相对原题稍作改动
#
#  示例：
#
#  输入： 1->2->3->4->5 和 k = 2
# 输出： 4
#
#  说明：
#
#  给定的 k 保证是有效的。
#  Related Topics 链表 双指针
#  👍 76 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        H = head
        while k > 0:
            head = head.next
            k -= 1
        ans = H
        while head:
            head = head.next
            ans = ans.next
        return ans.val
