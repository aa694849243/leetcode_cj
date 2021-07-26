#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
#
#  示例1:
#
#
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
#
#
#  示例2:
#
#
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
#
#
#  提示：
#
#
#  链表长度在[0, 20000]范围内。
#  链表元素在[0, 20000]范围内。
#
#
#  进阶：
#
#  如果不得使用临时缓冲区，该怎么解决？
#  Related Topics 哈希表 链表 双指针
#  👍 112 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        H = head
        m = set()
        while head:
            if head.val in m:
                pre.next = head.next
            else:
                m.add(head.val)
                pre = head
            head = head.next
        return H
from leetcode.trick.listnode.L import stringToListNode
a=stringToListNode('[1, 2, 3, 3, 2, 1]')
Solution().removeDuplicateNodes(a)