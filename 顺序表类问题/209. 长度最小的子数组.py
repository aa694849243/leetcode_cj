'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum_ = 0
        flag = 0
        ans = float('inf')
        while right < len(nums):
            if nums[right] >= s:  # 单个数字大于目标值，直接返回1
                return 1
            sum_ += nums[right]
            while sum_ >= s:
                sum_ -= nums[left]
                left += 1
                flag = 1  # 判断是否进入过循环，如果没有进入过循环，说明没有符合条件的连续数组
            if flag:
                ans = min(ans, right - left + 2)  # right-left+2是因为当前数组为目前最大小于目标值的连续数组，所以需要再扩充1格
            right += 1
        if not flag:
            return 0
        else:
            return ans


# 时间复杂度为nlogn的解法为将前缀和存入一个数组，然后将目标值减去前缀和，通过二分查找找到对应移动的位置
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / minimum - size - subarray - sum / solution / chang - du - zui - xiao - de - zi - shu - zu - by - leetcode - solutio /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


Solution().minSubArrayLen(11, [1, 2, 3, 4, 5])
