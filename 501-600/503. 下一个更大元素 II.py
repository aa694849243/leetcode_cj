'''给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        stack = []
        ans = [-1] * len(nums)
        p = 0
        while p < len(nums):
            if stack and nums[p] <= nums[stack[-1]]:
                stack.append(p)
                p += 1
                continue
            while stack and nums[stack[-1]] < nums[p]:
                ans[stack.pop()] = nums[p]
            stack.append(p)
            p += 1
        r = stack[0]
        for i in range(r+1):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
        return ans
Solution().nextGreaterElements([1,2,1])