'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
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


def swapPairs(head: ListNode) -> ListNode:
    if not head.next:
        return head
    H = ListNode(0)
    H_ = H
    while head and head.next:
        temp = head.next.next
        H.next = head.next
        H.next.next = head
        head = temp
        H = H.next.next
        H.next = head
    if head:
        H.next = head
    return H_.next


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


A = stringToListNode([1, 2, 3, 4])
listNodeToString(swapPairs(A))
