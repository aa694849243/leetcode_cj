'''给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

示例:

// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-random-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_0 = obj.getRandom()
import random

from leetcode.trick.listnode.L import stringToListNode


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.c = 0
        while head:
            head = head.next
            self.c += 1

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if self.head:
            num = random.randint(0, self.c - 1)
            ans = self.head
            while num > 0:
                ans = ans.next
                num -= 1
            return ans.val


a = stringToListNode('[1,2,3]')
obj = Solution(a)
obj.getRandom()
