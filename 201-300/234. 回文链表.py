'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        count = 0
        H = head
        while head:
            head = head.next
            count += 1
        breakp = count // 2
        pre = ListNode(0)
        n = 0
        head = H
        while n < breakp:
            ne = head.next
            head.next = pre
            pre = head
            head = ne
            n += 1
        head=head if count % 2 == 0 else head.next
        while head:
            if head.val==pre.val:
                head=head.next
                pre=pre.next
            else:
                return False
        return True


