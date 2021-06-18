# -*- coding: utf-8 -*-


# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
#
#  删除完毕后，请你返回最终结果链表的头节点。
#
#
#
#  你可以返回任何满足题目要求的答案。
#
#  （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
#
#  示例 1：
#
#  输入：head = [1,2,-3,3,1]
# 输出：[3,1]
# 提示：答案 [1,2,1] 也是正确的。
#
#
#  示例 2：
#
#  输入：head = [1,2,3,-3,4]
# 输出：[1,2,4]
#
#
#  示例 3：
#
#  输入：head = [1,2,3,-3,-2]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  给你的链表中可能有 1 到 1000 个节点。
#  对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
#
#  Related Topics 链表
#  👍 124 👎 0


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix = 0
        H = ListNode(0)
        H.next = head
        m = {0: H}
        while head:
            prefix += int(head.val)
            if prefix in m:
                prenode = m[prefix]
                nxtnode = prenode.next
                while nxtnode != head:
                    prefix += int(nxtnode.val)
                    nxtnode = nxtnode.next
                    m.pop(prefix)
                prefix += int(head.val)
                prenode.next = head.next
            else:
                m[prefix] = head
            head = head.next
        return H.next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        dic = {}
        s = 0
        p = dummy
        while p:
            s += p.val
            dic[s] = p
            p = p.next
        s = 0
        p = dummy
        while p:
            s += p.val
            p.next = dic[s].next
            p = p.next
        return dummy.next

# 作者：juicern
# 链接：https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/solution/liang-ci-bian-li-duo-chong-yu-yan-by-jui-pz7q/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from leetcode.trick.listnode.L import stringToListNode

a = stringToListNode('[1,2,3,-3,-2]')
Solution().removeZeroSumSublists(a)
