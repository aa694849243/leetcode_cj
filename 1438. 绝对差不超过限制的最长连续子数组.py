# -*- coding: utf-8 -*-
import collections
from typing import List

# 1利用sortedcontainers
from sortedcontainers import SortedList


# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limi
# t 。
#
#  如果不存在满足条件的子数组，则返回 0 。
#
#
#
#  示例 1：
#
#  输入：nums = [8,2,4,7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。
#
#
#  示例 2：
#
#  输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
#
#
#  示例 3：
#
#  输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^9
#  0 <= limit <= 10^9
#
#  Related Topics 队列 数组 有序集合 滑动窗口 单调队列 堆（优先队列）
#  👍 199 👎 0
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        li = SortedList()
        l = 0
        ans = 0
        for i, num in enumerate(nums):
            li.add(num)
            while li[-1] - li[0] > limit:
                li.remove(nums[l])
                l += 1
            ans=max(ans,i-l+1)
        return ans
#2双单调队列
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        qde=collections.deque() #递减栈
        qae=collections.deque() #递增栈
        l,r=0,0
        ans=1
        while r<len(nums):
            while qde and nums[r]>nums[qde[-1]]: #存入栈里的要尽可能往左
                qde.pop()
            while qae and nums[r]<nums[qae[-1]]:
                qae.pop()
            qde.append(r)
            qae.append(r)
            while qde and qae and nums[qde[0]]-nums[qae[0]]>limit:
                if qde[0]==l:
                    qde.popleft()
                if qae[0]==l:
                    qae.popleft()
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans


Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5)
