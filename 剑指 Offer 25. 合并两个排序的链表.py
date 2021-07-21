#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
#  示例1：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  限制：
#
#  0 <= 链表长度 <= 1000
#
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
#  Related Topics 递归 链表
#  👍 141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        H=ListNode(0)
        head=H
        while l1 and l2:
            if l1.val>l2.val:
                head.next=l2
                l2=l2.next
            else:
                head.next=l1
                l1=l1.next
            head=head.next
        if l1:
            head.next=l1
        elif l2:
            head.next=l2
        return H.next
