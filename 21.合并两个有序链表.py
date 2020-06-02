'''
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


# ----------------------caojie---29%-----------------------------------------------------------------------------------
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    ans = head
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = l1
            head = head.next
            l1 = l1.next
        else:
            head.next = l2
            head = head.next
            l2 = l2.next
    if l1:
        head.next = l1
    elif l2:
        head.next = l2
    return ans.next


# -----------------------递归用法--------------------------------------------------------------------------
def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    if l1.val <= l2.val:#永远返回值小的那个，且值小的那个的next连接下一步更小的值
        l1.next = mergeTwoLists(l1.next, l2)  # l1<l2,则返回l1（第一步返回的是head），并且l1.next为l1.next.val和l2.v
        # al小的那个，继续将l1.next和l2进行mergetwolists
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


l1 = [1, 2, 4]
l2 = [1, 3, 4]
l1 = stringToListNode(l1)
l2 = stringToListNode(l2)
mergeTwoLists(l1, l2)
