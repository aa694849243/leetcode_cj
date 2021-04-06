'''给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        l = 0
        k = 0
        ans = 0
        while l < len(nums) - 2:
            r = l + 1
            while r < len(nums) - 1 and k <= len(nums):
                k = max(k, r + 1)
                while k < len(nums) and nums[l] + nums[r] > nums[k]:
                    k += 1
                ans += k - r - 1
                r += 1
            l += 1
            k = 0
        return ans


Solution().triangleNumber([1,2,3,4,5,6])
