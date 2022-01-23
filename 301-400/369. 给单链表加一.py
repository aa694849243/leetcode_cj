#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。
#
#  你可以假设这个整数除了 0 本身，没有任何前导的 0。
#
#  这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
#
#  Related Topics 链表 数学
#  👍 81 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 哨兵头节点
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        H = ListNode(0)
        H.next = head
        notnine = H
        while head:
            if head.val != 9:
                notnine = head
            head = head.next
        notnine.val += 1
        p = notnine.next
        while p:
            p.val = 0
            p = p.next
        if notnine == H:
            return notnine
        return H.next
