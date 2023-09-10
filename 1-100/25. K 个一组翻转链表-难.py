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


from typing import List, Optional


class Solution:
    def reverse_list(self, head, k):
        pre = None
        cur = head
        tail = head
        while cur and k > 0:
            cur.next, pre, cur = pre, cur, cur.next
            k -= 1
        next_cur = cur
        if k > 0:
            cur = pre
            tail = cur
            pre = None
            next_cur = None
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
        return pre, tail, next_cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        H = ListNode(0)
        last_tail = H
        cur = head
        while cur:
            pre, tail, next_cur = self.reverse_list(cur, k)
            last_tail.next = pre
            cur = next_cur
            last_tail = tail
        return H.next


# leetcode submit region end(Prohibit modification and deletion)
Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)
