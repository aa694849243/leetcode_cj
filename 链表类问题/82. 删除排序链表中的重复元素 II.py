'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp = head.val
        tmpNode = head
        head = head.next
        H = ListNode(0)
        ans = H
        count = 0
        while head:
            if head.val == tmp:
                count += 1
            else:
                if count == 0:
                    H.next = tmpNode
                    H = H.next
                else:
                    count = 0
                tmpNode = head
                tmp = head.val
            head = head.next
        if count == 0:
            H.next = tmpNode
            H = H.next
        H.next = None
        return ans.next


def stringToListNode(input):
    # Generate list from the input
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


a = [1, 2, 3, 3, 4, 4, 5]
s = stringToListNode(a)
Solution().deleteDuplicates(s)
