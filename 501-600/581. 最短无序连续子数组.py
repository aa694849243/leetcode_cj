'''给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        m = sorted(nums.copy())
        l, r = 0, 0
        for i in range(len(nums)):
            if nums[i] != m[i]:
                l = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != m[i]:
                r = i
                break
        return r - l + 1 if l != r else 0


Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
