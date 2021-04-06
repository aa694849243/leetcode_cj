'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = {}
        index = 0
        while head:
            if head not in s:
                s[head] = index
            else:
                return head
            head = head.next
            index += 1
        return


# 双指针 快慢指针 数学
# 数学分析见官方题解
# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        H=head
        fcur, scur = head, head
        while head and head.next:
            fcur = fcur.next.next
            scur = scur.next
            if fcur == scur:
                while True:
                    if scur==H:
                        return H
                    else:
                        scur,H=scur.next,H.next
            head = head.next.next
        return
