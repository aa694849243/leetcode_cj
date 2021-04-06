'''
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        left, right = 0, 1
        ans = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if right - left > 1:
                    ans.append('{}->{}'.format(nums[left], nums[right - 1]))
                    left = right
                else:
                    ans.append(str(nums[left]))
                    left=right
            right += 1
        if len(nums[left:])==1:
            ans.append(str(nums[left]))
        else:
            ans.append('{}->{}'.format(nums[left],nums[right-1]))
        return ans
a= [0,2,3,4,6,8,9]
Solution().summaryRanges(a)