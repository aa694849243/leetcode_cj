# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。
#
#  如果数组中不存在满足题意的整数，则返回 0 。
#
#
#
#  示例：
#
#  输入：nums = [21,4,7]
# 输出：32
# 解释：
# 21 有 4 个因数：1, 3, 7, 21
# 4 有 3 个因数：1, 2, 4
# 7 有 2 个因数：1, 7
# 答案仅为 21 的所有因数的和。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^4
#  1 <= nums[i] <= 10^5
#
#  Related Topics 数组 数学
#  👍 15 👎 0


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            li=set()
            if int(num**0.5)==num:
                continue
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    li|={i,num//i}
            if len(li)==2:
                ans+=sum(li)+num+1
        return ans
Solution().sumFourDivisors([21,4,7])