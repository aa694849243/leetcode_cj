# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 23:33 
# ide： PyCharm
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        H = head
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        idx = cnt - n
        if idx == 0:
            return H.next
        p = 0
        head = H
        while p < idx - 1:
            head = head.next
            p += 1
        head.next = head.next.next
        return H


# leetcode submit region end(Prohibit modification and deletion)
from typing import List


def stringToListNode(input):
    # Generate list from the input
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None
    numbers = [s.strip() for s in input.split(',')]

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


root = stringToListNode('[1,2,3,4,5]')
print(
    Solution().removeNthFromEnd(
        root, 2
    )
)
