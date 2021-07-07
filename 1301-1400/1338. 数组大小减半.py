# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你一个整数数组 arr。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。
#
#  返回 至少 能删除数组中的一半整数的整数集合的最小大小。
#
#
#
#  示例 1：
#
#  输入：arr = [3,3,3,3,5,5,5,2,2,7]
# 输出：2
# 解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
# 大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
# 选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。
#
#
#  示例 2：
#
#  输入：arr = [7,7,7,7,7,7]
# 输出：1
# 解释：我们只能选择集合 {7}，结果数组为空。
#
#
#  示例 3：
#
#  输入：arr = [1,9]
# 输出：1
#
#
#  示例 4：
#
#  输入：arr = [1000,1000,3,7]
# 输出：1
#
#
#  示例 5：
#
#  输入：arr = [1,2,3,4,5,6,7,8,9,10]
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 10^5
#  arr.length 为偶数
#  1 <= arr[i] <= 10^5
#
#  Related Topics 贪心 数组 哈希表 排序 堆（优先队列）
#  👍 23 👎 0


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = collections.Counter(arr)
        li = sorted(m, key=lambda x:-m[x])
        n=len(arr)
        cnt=0
        ans=0
        for i in li:
            cnt+=m[i]
            ans+=1
            if cnt>=(n-1)//2+1:
                return ans

