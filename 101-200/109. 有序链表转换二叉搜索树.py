'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
from leetcode.trick.listnode.L import stringToListNode


# 双指针，快指针，慢指针 递归
class Solution:
    def findroot(self, head):
        slowcur, fastcur = head, head
        precur = None
        while fastcur and fastcur.next:
            precur = slowcur
            slowcur = slowcur.next
            fastcur = fastcur.next.next
        if precur:
            precur.next = None
        return slowcur

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        lnode = self.findroot(head)
        root = TreeNode(lnode.val)
        if lnode == head:
            return TreeNode(head.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(lnode.next)
        return root


# 递归 精妙递归 链表递归 二叉树递归
class Solution:
    def findsize(self, head):
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
        return size

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.findsize(head)

        def buildtree(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l + r) // 2
            left = buildtree(l, mid - 1)
            node = TreeNode(head.val)
            head = head.next
            node.left = left
            node.right = buildtree(mid + 1, r)
            return node

        if size == 0:
            return None
        return buildtree(0, size - 1)


a = stringToListNode('[-10,-3,0,5,9]')
Solution().sortedListToBST(a)
