# 给你一个链表数组，每个链表都已经按升序排列。
#
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
#  示例 1：
#
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
#  示例 2：
#
#  输入：lists = []
# 输出：[]
#
#
#  示例 3：
#
#  输入：lists = [[]]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  k == lists.length
#  0 <= k <= 10^4
#  0 <= lists[i].length <= 500
#  -10^4 <= lists[i][j] <= 10^4
#  lists[i] 按 升序 排列
#  lists[i].length 的总和不超过 10^4
#
#
#  Related Topics 链表 分治 堆（优先队列） 归并排序
#  👍 2478 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            dummy = ListNode(0)
            p = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    p = p.next
                    l1 = l1.next
                else:
                    p.next = l2
                    p = p.next
                    l2 = l2.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next

        n = len(lists)
        step = 1
        while step < n:
            for i in range(0, n - step, step * 2):  # trick
                lists[i] = merge2Lists(lists[i], lists[i + step])
            step *= 2
        return lists[0] if n > 0 else None
# leetcode submit region end(Prohibit modification and deletion)
