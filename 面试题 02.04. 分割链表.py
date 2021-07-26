#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
#  你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 200] 内
#  -100 <= Node.val <= 100
#  -200 <= x <= 200
#
#  Related Topics 链表 双指针
#  👍 65 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1, h2 = ListNode(-1), ListNode(-1)
        H1, H2 = h1, h2
        h1.next = head
        h2.next = head
        while head:
            if int(head.val) >= x:
                h1.next=head
                h1=h1.next
                # h1.next=None
            else:
                h2.next=head
                h2=h2.next
                # h2.next=None
            head=head.next
        h1.next=None
        h2.next=None
        h2.next=H1.next
        return H2.next

from leetcode.trick.listnode.L import stringToListNode
a=stringToListNode('[1,4,3,2,5,2]')
Solution().partition(a,3)