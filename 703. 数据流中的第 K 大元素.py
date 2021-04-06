'''设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
 

示例：

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

提示：
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
最多调用 add 方法 104 次
题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Lnode:
    def __init__(self, val, next=None, pre=None):
        self.val = val
        self.next = next


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.head = Lnode(0)
        self.k = k
        a = self.head
        self.cnt = 0
        nums = nums[:k]
        nums = nums[::-1]
        for i in range(len(nums)):
            a.next = Lnode(nums[i])
            a = a.next
            self.cnt += 1

    def add(self, val: int) -> int:
        a = self.head
        if not a.next:
            self.head.next = Lnode(val)
            self.cnt += 1
            return val
        if self.cnt < self.k:
            self.cnt += 1
            while a.next and a.next.val < val:
                a = a.next
            b=a.next
            a.next=Lnode(val)
            a.next.next=b
            return self.head.next.val
        if val <= self.head.next.val:
            return self.head.next.val
        while a.next and a.next.val < val:
            a = a.next
        b = a.next
        a.next = Lnode(val)
        a.next.next = b
        self.head.next = self.head.next.next
        return self.head.next.val


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(2, [0])
param_1 = obj.add(0)
obj.add(5)
