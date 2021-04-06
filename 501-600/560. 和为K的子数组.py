'''给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import itertools
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        precum = [0, *itertools.accumulate(nums)]
        m = collections.defaultdict(set)
        for i, num in enumerate(precum):
            m[num].add(i)
        cnt = 0
        for i in range(1, len(precum)):
            x = precum[i] - k
            if x in m:
                for j in m[x]:
                    if j < i:
                        cnt += 1
        return cnt

Solution().subarraySum([1,2,3], 3)