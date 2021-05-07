# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
#  示例 1：
#
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  -50000 <= nums[i] <= 50000
#
#  👍 286 👎 0

from typing import List


# 1快排
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def q_sort(l, r):
            if l >= r:
                return
            tmp = nums[l]
            i = l
            for j in range(l + 1, r + 1):
                if nums[j] < tmp:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            q_sort(l, i - 1)
            q_sort(i + 1, r)

        q_sort(0, len(nums) - 1)


# 2归并
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, mid, r, fro, to):
            i, j, k = l, mid, l
            while i < mid and j < r:
                if fro[i] <= fro[j]:
                    to[k] = fro[i]
                    i += 1
                    k += 1
                else:
                    to[k] = fro[j]
                    j += 1
                    k += 1
            if i < mid:
                while i < mid:
                    to[k] = fro[i]
                    i += 1
                    k += 1
            if j < r:
                while j < r:
                    to[k] = fro[j]
                    j += 1
                    k += 1

        def merge_pass(slen, fro, to):
            i = 0
            r = len(fro)
            while i + 2 * slen <= r:
                merge(i, i + slen, i + 2 * slen, fro, to)
                i += 2 * slen
            if i + slen < r:
                merge(i, i + slen, r, fro, to)
            elif i + slen >= r:
                for j in range(i, r):
                    to[j] = fro[j]

        def merge_sort(li):
            tmp = li.copy()
            slen = 1
            while slen < len(li):
                merge_pass(slen, li, tmp)
                slen *= 2
                merge_pass(slen, tmp, li)
                slen *= 2

        merge_sort(nums)
        return nums


# 3堆排序

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heap_sort(nums):
            def siftdown(nums, e, begin, end):
                i, j = begin, begin * 2 + 1
                while j < end:
                    if j + 1 < end and nums[j + 1] > nums[j]:
                        j += 1
                    if e > nums[j]:
                        break
                    nums[i] = nums[j]
                    i, j = j, 2 * j + 1
                nums[i] = e

            end = len(nums)
            for i in range(len(nums) // 2, -1, -1):
                siftdown(nums, nums[i], i, end)
            for i in range(len(nums) - 1, 0, -1):
                e = nums[i]
                nums[i] = nums[0]
                siftdown(nums, e, 0, i)
            return nums

        return heap_sort(nums)


# 4 基数排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ma = max(nums)
        leng = len(str(ma))
        i = 0
        while i < leng:
            buckets = [[] for _ in range(10)]
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            nums.clear()
            for row in buckets:
                for val in row:
                    nums.append(val)
            i += 1
        return nums


# 5 希尔排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                tmp = nums[i]
                while i - gap >= 0 and nums[i - gap] >= tmp:
                    nums[i] = nums[i - gap]
                    i -= gap
                nums[i] = tmp
            gap//=2
        return nums


Solution().sortArray([12, 34, 54, 2, 3])
