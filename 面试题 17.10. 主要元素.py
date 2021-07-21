# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1
# ) 的解决方案。
#
#
#
#  示例 1：
#
#
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5
#
#  示例 2：
#
#
# 输入：[3,2]
# 输出：-1
#
#  示例 3：
#
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#  Related Topics 数组 计数
#  👍 134 👎 0

#摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        flag,cnt=nums[0],1
        for num in nums[1:]:
            if num==flag:
                cnt+=1
            else:
                cnt-=1
                if cnt<0:
                    flag,cnt=num,1
        if cnt==0:
            return -1
        cnt=0
        for num in nums:
            if num==flag:
                cnt+=1
        return flag if cnt>len(nums)//2 else -1
Solution().majorityElement([6,5,5])