#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
#
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 5000
#
#
#
#  注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
#  Related Topics 递归 链表
#  👍 262 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        while head:
            nxt=head.next
            head.next=pre
            pre=head
            head=nxt
        return pre