#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环非降序的。
#
#  给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
#
#  如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
#
#  如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。
#
#
#
#  示例 1：
#
#
#
# 输入：head = [3,4,1], insertVal = 2
# 输出：[3,4,1,2]
# 解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后
# ，整个列表如上图所示，最后返回节点 3 。
#
#
#
#
#  示例 2：
#
#
# 输入：head = [], insertVal = 1
# 输出：[1]
# 解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。
#
#
#  示例 3：
#
#
# 输入：head = [1], insertVal = 0
# 输出：[1,0]
#
#
#
#
#  提示：
#
#
#  0 <= Number of Nodes <= 5 * 104
#  -106 <= Node.val, insertVal <= 106
#
#  Related Topics 链表
#  👍 49 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        if head.next == head:
            head.next = node
            node.next = head
            return head
        flag = head
        pre = head
        head = head.next
        flag_ = False
        while head:
            if pre.val <= insertVal <= head.val or pre.val > head.val and (insertVal >= pre.val or insertVal<=head.val):
                pre.next = node
                node.next = head
                break
            if pre == flag and flag_:
                pre.next = node
                node.next = head
                break
            flag_ = True
            pre = head
            head = head.next
        return flag


from trick.listnode.L import stringToListNode

a = stringToListNode('[1,3,5]')
Solution().insert(a, 6)
