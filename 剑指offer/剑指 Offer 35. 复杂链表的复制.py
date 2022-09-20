#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指
# 向链表中的任意节点或者 null。
#
#
#
#  示例 1：
#
#
#
#  输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
#  示例 2：
#
#
#
#  输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
#
#  示例 3：
#
#
#
#  输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
#  示例 4：
#
#  输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#
#
#
#
#  提示：
#
#
#  -10000 <= Node.val <= 10000
#  Node.random 为空（null）或指向链表中的节点。
#  节点数目不超过 1000 。
#
#
#
#
#  注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-point
# er/
#
#
#  Related Topics 哈希表 链表
#  👍 238 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 1哈希
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        m = {}
        while cur:
            m[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            m[cur].next = m.get(cur.next)
            m[cur].random = m.get(cur.random)
            cur = cur.next
        return m[head]


# 2拆分链表
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        cur = head
        while cur:
            node = cur.next
            node.random = cur.random.next if cur.random else None
            cur = cur.next.next
        cur = head
        ans=Node(-1)
        node=ans
        while cur and cur.next:
            node.next=cur.next
            cur=cur.next.next
            node=node.next
        return ans.next