'''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#空间复杂度为n的方法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head not in s:
                s.add(head)
            else:
                return True
            head = head.next
        return False
#快慢指针 双指针 时间复杂度为O(n) 具体分析看官方题解
# https://leetcode-cn.com/problems/linked-list-cycle/solution/huan-xing-lian-biao-by-leetcode/
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fcur,scur=head,head
        while head and head.next:
            fcur=fcur.next.next
            scur=scur.next
            if fcur==scur:
                return True
        return False
