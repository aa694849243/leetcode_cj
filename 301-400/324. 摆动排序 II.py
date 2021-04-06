'''给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:

输入: nums = [1, 5, 1, 1, 6, 4]
输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
示例 2:

输入: nums = [1, 3, 2, 2, 3, 1]
输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
说明:
你可以假设所有输入都会得到有效的结果。

进阶:
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-sort-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# C:\Users\caoji\PycharmProjects\learn\leetcode\324. 摆动排序 II.py
from typing import List


# 快速选择 平均时间复杂度O(n),最坏时间复杂度O(n^2) 快速选择法
# 荷兰旗 3-way-partition 3路归并
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        # 一次划分 快排
        def one_qsort(left, right):
            pivot = nums[left]
            j = left
            for i in range(left + 1, right + 1):
                if nums[i] < pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[j] = nums[j], nums[left]
            return j

        # 找中点
        left, right = 0, len(nums) - 1
        mid = right // 2
        x = one_qsort(left, right)
        while x != mid:
            if x < mid:
                left = x + 1
            elif x > mid:
                right = x - 1
            x = one_qsort(left, right)

        cur = 0
        left, right = 0, len(nums) - 1
        # 三路划分（荷兰旗）
        while cur < right:
            if nums[cur] < nums[mid]:
                nums[left], nums[cur] = nums[cur], nums[left]
                cur += 1
                left += 1
            elif nums[cur] > nums[mid]:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            elif nums[cur] == nums[mid]:
                cur += 1

        # 交叉合并
        nc = nums[:]
        small, big = mid, len(nums) - 1
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = nc[small]
                small -= 1
            else:
                nums[i] = nc[big]
                big -= 1
        return


nums = list(range(5000))
nums.reverse()
Solution().wiggleSort(nums)


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return nums
        mid = (0 + n - 1) // 2  # 中位数索引

        # 快速排序中的一次划分
        def partition(begin, end):
            left, right = begin, end
            while left < right:
                while left < right and nums[left] < nums[right]: right -= 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                while left < right and nums[left] < nums[right]: left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            return left

        # 找到中位数对应的数值
        left, right = 0, n - 1
        while True:
            pivot = partition(left, right)
            if pivot == mid:
                break
            elif pivot > mid:
                right = pivot - 1
            else:
                left = pivot + 1

        # 三路划分(荷兰旗)
        midNum = nums[mid]
        left, curr, right = 0, 0, n - 1
        while curr < right:
            if nums[curr] < midNum:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] > midNum:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

        # 交叉合并
        small, big, _nums = mid, n - 1, nums[:]
        for i in range(n):
            if i % 2 == 0:
                nums[i] = _nums[small]
                small -= 1
            else:  # big
                nums[i] = _nums[big]
                big -= 1
        return


nums = list(range(5000))
nums.reverse()
Solution().wiggleSort(nums)
