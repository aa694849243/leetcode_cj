'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        H = head
        if not head or not head.next or not head.next.next:
            return head
        head = head.next
        a, b = [], []
        while head:
            a.append(head)
            b.append(head)
            head = head.next
        b.reverse()
        i = 0
        head = H
        while a[i] != b[i] and b[i].next != a[i]:
            b[i].next = a[i]
            head.next = b[i]
            head = a[i]
            i += 1
        head.next = None
        return H


from leetcode.trick.listnode.L import stringToListNode


# 空间复杂度为1的方法，快慢指针 双指针
class Solution:
    def reorderList(self, head: ListNode) -> None:
        def inversion(head):
            if not head or not head.next:
                return head
            pre = head
            head = head.next
            pre.next = None
            while head:
                p = head.next
                head.next = pre
                pre = head
                head = p
            return pre

        H = head
        fcur, scur = head, head
        while head and head.next:
            fcur = fcur.next.next
            prev = scur
            scur = scur.next
            head = fcur
        if head:
            t = inversion(scur.next)
            scur.next = None
        else:
            t = inversion(scur)
            prev.next = None
        head = H
        while head and t:
            x = head.next
            y = t.next
            head.next = t
            t.next = x
            head = x
            t = y

        return H


a = stringToListNode('[1,2,3,4,5]')

Solution().reorderList(a)
