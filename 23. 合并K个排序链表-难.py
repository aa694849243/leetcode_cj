'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists) -> ListNode:
    head = ListNode(0)
    H = head
    j=0
    def recursion(lists, head):
        mi = ListNode(float('inf'))
        j=0
        for i in range(len(lists)):
            if lists[i]:
                if lists[i].val <= mi.val:
                    mi = lists[i]
                    x = i
            elif not lists[i]:
                j+=1
                continue
        if j>=len(lists):
            return
        head.next = mi
        head = head.next
        lists[x] = lists[x].next
        return recursion(lists, head)
    recursion(lists, head)
    return H

def stringToListNode(numbers:list):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr
#----------链表转列表----------------------------------------------------------------------
def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"
A=[[1,4,5],[1,3,4],[2,6]]
for i in range(len(A)):
    A[i]=stringToListNode(A[i])
mergeKLists(A)



