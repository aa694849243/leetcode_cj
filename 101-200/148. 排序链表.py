# coding=utf-8
'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 归并法 链表归并
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def merge(node1, node2, pre, slen):  # 定义归并策略，分为l1,l2两段
            if not node2:  # 如果l1不足slen，那么归并到了尽头，node2必为none，那直接返回尾部节点
                while node1:
                    pre = node1
                    node1 = node1.next
                return pre
            l1, l2 = 0, 0
            while l1 < slen and l2 < slen:  # 归并策略，按顺序归并
                if int(node1.val) < int(node2.val):
                    pre.next = node1
                    node1 = node1.next
                    pre = pre.next
                    l1 += 1
                else:
                    pre.next = node2
                    node2 = node2.next
                    pre = pre.next
                    l2 += 1
                    if not node2:  # 特殊情况，l2不够slen且更早走到尽头，那么将node1循环到l1终点，并将终点链接None,并返回终点
                        pre.next = node1
                        while l1 < slen:
                            pre = pre.next
                            l1 += 1
                        pre.next = None
                        return pre
            if l1 == slen:  # 如果l1先走完的情况
                pre.next = node2
                while l2 < slen and pre.next:  # 需要特判一下是否走到最终点，因为假如最后一个元素属于l2，但l2比较短，l2走不到slen，即特判pre.next不存在
                    pre = pre.next
                    l2 += 1
            else:  # 如果l2先走完的情况
                pre.next = node1
                while l1 < slen:
                    pre = pre.next
                    l1 += 1
                pre.next = node2
            return pre

        lenth = 0
        H = ListNode(0)
        H.next = head
        while head:  # 算lenth
            head = head.next
            lenth += 1
        slen = 1
        while slen < lenth:  # 当slen<lenth一直循环
            prev = H  # H保存起始点
            head = H.next
            node1 = head
            while node1:  # 找到l1，l2归并的起点node1，node2
                l = 0
                node2 = node1
                while l < slen and node2:  # 预防最后一段仅有l1.没有node2，需要特判node2存不存在
                    node2 = node2.next
                    l += 1
                prev = merge(node1, node2, prev, slen)
                node1 = prev.next
            slen *= 2  # 更新步长
        return H.next


from leetcode.trick.listnode.L import listNodeToString
from leetcode.trick.listnode.L import stringToListNode


# 递归+快速排序 超时
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def rec(pre, head, tail):
            if head.next == tail or head == tail:
                return
            node = head.next
            p = head
            while node != tail:
                if int(node.val) < int(head.val):
                    p.next = node.next
                    node.next = pre.next
                    pre.next = node
                    node = p.next
                else:
                    p = node
                    node = node.next
            rec(pre, pre.next, head)
            rec(head, head.next, tail)

        if not head:
            return
        H = ListNode(0)
        T = ListNode(9.9)
        H.next = head
        while head:
            pre = head
            head = head.next
        pre.next = T
        rec(H, H.next, T)
        head = H.next
        while head:
            if head.next == T:
                head.next = None
            head = head.next
        return H.next


# 归并+递归 链表递归 特殊递归
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
b = stringToListNode('[3,4,1,9,18,27,36]')
Solution().sortList(b)
