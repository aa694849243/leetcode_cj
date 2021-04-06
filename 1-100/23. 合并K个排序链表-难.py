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


# -----------------------------------------堆排序法------------------------------------------------------------------------
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/xiong-mao-shua-ti-python3-3chong-jie-fa-bao-li-you/
#建堆的时间复杂度为O(knlogkn),弹出的时间复杂度为(logkn),所以总时间复杂度应该为（knlogkn）
def mergeKLists(lists):  # 堆排序法，利用heapq模块进行建堆（小顶堆），再不断弹出
    if not lists or len(lists) == 0:
        return None
    import heapq
    heap = []
    # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
    for node in lists:
        while node:
            heapq.heappush(heap, node.val)
            node = node.next

    dummy = ListNode(None)
    cur = dummy
    # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
    while heap:
        temp_node = ListNode(heap.heappop(heap))
        cur.next = temp_node
        cur = temp_node
    return dummy.next


# ---------------------------------------------归并法-----------------------------------------------------------------------
#归并的时间复杂度为log(k)-k为len(lists),每次合并的时间复杂度为O(L1+L2)==O(2n)..第一轮为2n，第2轮为4n。。。总的时间复杂度为O(nklogk)
#具体分析https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/
class Solution:
    def merge(self,lnode1, lnode2):
        if not lnode1:
            return lnode2
        if not lnode2:
            return lnode1
        if lnode1.val <= lnode2.val:
            lnode1.next = self.merge(lnode1.next, lnode2)
            return lnode1
        else:
            lnode2.next = self.merge(lnode1, lnode2.next)
            return lnode2


    def mergepass(self,lists, slen):
        i, lenth = 0, len(lists)
        while i + 2 * slen <= lenth:
            lists[i] = self.merge(lists[i], lists[i + slen])
            i += 2 * slen
        if i+slen<lenth:
            lists[i]=self.merge(lists[i],lists[i+slen])

    def mergeKLists(self, lists) -> ListNode:
        if len(lists)==0:
            return []
        slen = 1
        while slen < len(lists):
            self.mergepass(lists,slen)
            slen *= 2
        return lists[0]
#caojie题解---------https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/gui-bing-fa-by-aa694849243/

def stringToListNode(numbers: list):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


# ----------链表转列表----------------------------------------------------------------------
def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


A = [[1, 4, 5], [1, 3, 4], [2, 6]]
for i in range(len(A)):
    A[i] = stringToListNode(A[i])
Solution().mergeKLists(A)
