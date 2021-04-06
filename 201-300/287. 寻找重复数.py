'''给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 二分法 特殊二分法
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        n = len(nums)
        while left < right:
            count = 0
            mid = (left + right) // 2
            for i in range(n):
                if nums[i] <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid

        return left


# 位操作
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = len(nums) - 1
        one = 1

        ans = 0
        j = 0
        while x > 0:
            count = 0
            count2 = 0
            for i in range(1, len(nums)):
                count += ((i >> j) & 1)
                count2 += ((nums[i] >> j) & 1)
            count2 += ((nums[0] >> j) & 1)
            if count2 > count:
                ans += (one << j)
            j += 1
            x >>= 1
        return ans


# 龟兔赛跑算法
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[nums[0]]
        fast=nums[nums[nums[0]]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


Solution().findDuplicate([1,4,4,2,4])
