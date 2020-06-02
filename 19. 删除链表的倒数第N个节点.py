'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    H = head
    a = []
    i = 0
    while head:
        a.append(head)
        head = head.next
        i += 1
    t = i - n
    if i == 1:
        return
    if i == n:
        return H.next
    else:
        head = H
    i = 0
    while i < t:
        head = head.next
        i += 1
    head.next = head.next.next
    return H

#--------------------------------------一趟遍历-----------------------------------------------------------------
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    H = head
    a = []
    i = 0
    while head:
        a.append(head)
        head = head.next
        i += 1
    if i == 1:
        return
    if i == n:
        return H.next
    a[i-n-1].next = a[i-n-1].next.next
    return H


numbers = stringToListNode([1, 2, 3, 4, 5])
n = 2
removeNthFromEnd(numbers, n)
