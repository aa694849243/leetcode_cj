'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

# 摩尔投票法
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        a, b = [nums[0], 0], [nums[0], 0]
        i = 0
        while i < len(nums):
            if nums[i] == a[0]:
                a[1] += 1
            elif nums[i] == b[0]:
                b[1] += 1
            else:
                if a[0] == b[0]:
                    b[0] = nums[i]
                    b[1] += 1
                else:
                    a[1] -= 1
                    b[1] -= 1
                    if a[1] < 0:
                        a = [nums[i], 1]
                        b[1] += 1
                    elif b[1] < 0:
                        b = [nums[i], 1]
                        a[1] += 1
            i += 1
        count1, count2 = 0, 0
        ans = []
        if a[1] > 0:
            for i in nums:
                if i == a[0]:
                    count1 += 1
        if b[1] > 0:
            for i in nums:
                if i == b[0]:
                    count2 += 1
        if count1 > len(nums) // 3:
            ans.append(a[0])
        if count2 > len(nums) // 3:
            ans.append(b[0])
        return ans


a = [1, 3, 3, 4, 4]
Solution().majorityElement(a)
