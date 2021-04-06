"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# --------------------caojie_26%----------------------------------------------------------------------------------------
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    a = []
    i = 0
    new = ListNode(0)  # 新做new链来接从head链上取下的节点
    H = new  # 保存头节点
    while head:
        a.append(head)
        head = head.next
        i += 1
        if i == k:
            while i > 0:
                new.next = a.pop()
                i -= 1
                new = new.next
            new.next = head
    j = 0
    while j < i:
        new.next = a[j]
        new = new.next
        j += 1
    new.next = head
    return H.next



#----------------------模拟法------------------------------------------------------------------------
class Solution:
    # 翻转一个子链表，并且返回新的头与尾，反转链表
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/






def stringToListNode(numbers: list):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


list1 = [1, 2, 3, 4, 5]
k = 2
head = stringToListNode(list1)
reverseKGroup(head, k)
