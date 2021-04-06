'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# caojie 冒泡排序 5%
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = 0
        while x < k:
            for i in range(len(nums) - 1 - x):
                if nums[i] >= nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            x += 1
        return nums[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2
Solution().findKthLargest(nums, k)


# 快速排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, begin, end):
            if begin >= end:
                return nums[begin]
            x = nums[begin]
            i = begin
            for j in range(begin + 1, end + 1):
                if nums[j] < x:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[begin], nums[i] = nums[i], nums[begin]
            if i == len(nums) - k:
                return nums[i]
            elif i > len(nums) - k:
                return quick_sort(nums, begin, i - 1)
            else:
                return quick_sort(nums, i + 1, end)

        return quick_sort(nums, 0, len(nums) - 1)


# 堆排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 筛选函数
        def siftdown(nums, e, begin, end):
            i, j = begin, 2 * begin + 1
            while j < end:
                if j + 1 < end and nums[j] < nums[j + 1]:
                    j += 1
                if e > nums[j]:
                    break
                nums[i] = nums[j]
                i, j = j, 2 * j + 1
            nums[i] = e

        # 建堆
        for i in range(len(nums) // 2, -1, -1):
            siftdown(nums, nums[i], i, len(nums))

        # 找值
        for i in range(len(nums) - 1, len(nums)-k-1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            siftdown(nums, nums[0], 0, i)
        return nums[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2
Solution().findKthLargest(nums, k)
