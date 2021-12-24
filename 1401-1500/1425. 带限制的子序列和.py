# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 num
# s[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。
#
#  数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。
#
#
#
#  示例 1：
#
#  输入：nums = [10,2,-10,5,20], k = 2
# 输出：37
# 解释：子序列为 [10, 2, 5, 20] 。
#
#
#  示例 2：
#
#  输入：nums = [-1,-2,-3], k = 1
# 输出：-1
# 解释：子序列必须是非空的，所以我们选择最大的数字。
#
#
#  示例 3：
#
#  输入：nums = [10,-2,-10,-5,20], k = 2
# 输出：23
# 解释：子序列为 [10, -2, -5, 20] 。
#
#
#
#
#  提示：
#
#
#  1 <= k <= nums.length <= 10^5
#  -10^4 <= nums[i] <= 10^4
#
#  Related Topics 队列 数组 动态规划 滑动窗口 单调队列 堆（优先队列）
#  👍 72 👎 0

# 单调队列+dp
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        f=[nums[0]]+[0]*(n-1)
        li=collections.deque([0])
        ans=nums[0]
        for i in range(1,n):
            while li and i-li[0]>k:
                li.popleft()
            f[i]=max(f[li[0]],0)+nums[i] #li一定会有元素的，因为li是单调递减队列，比栈顶小的会直接入栈，比栈顶大的会弹出一些元素后入栈，所以上一轮一定有一个元素入栈，所以栈中一定有元素
            ans=max(ans,f[i])
            while li and f[i]>=f[li[-1]]:
                li.pop()
            li.append(i)
        return ans


