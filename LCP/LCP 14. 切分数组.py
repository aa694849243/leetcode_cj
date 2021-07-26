# -*- coding: utf-8 -*-
import collections
from typing import List

# 给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请
# 求出最少可以切成多少个子数组。
#
#  示例 1：
#
#
#  输入：nums = [2,3,3,2,3,3]
#
#  输出：2
#
#  解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。
#
#
#  示例 2：
#
#
#  输入：nums = [2,3,5,7]
#
#  输出：4
#
#  解释：只有一种可行的切割：[2], [3], [5], [7]
#
#
#  限制：
#
#
#  1 <= nums.length <= 10^5
#  2 <= nums[i] <= 10^6
#
#  Related Topics 数组 数学 动态规划 数论
#  👍 39 👎 0

# 求最小质因数
maxnum = 10 ** 6
minfactors = [1] * (maxnum + 1)
p = 2
while p <= maxnum:
    i = p
    while i * p <= maxnum:
        minfactors[i * p] = p
        i += 1
    p += 1
    while p <= maxnum:
        if minfactors[p] == 1:
            break
        p += 1


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = collections.defaultdict(lambda: float('inf'))
        x = nums[0]
        while True:
            if minfactors[x] == 1:
                f[x] = 1
                break
            f[minfactors[x]] = 1  # 每个质因数的长度都设置为1
            x //= minfactors[x]
        prev = 1
        for i in range(1, n):
            x = nums[i]
            cur = float('inf')
            while True:
                if minfactors[x] == 1:
                    f[x] = min(f[x], prev + 1)  # 更新的f[x]跟cur是无关的，因为f[x]是计算x为左端点的最短步长，cur即可为左端点又可为右端点
                    cur = min(f[x], cur)
                    break
                f[minfactors[x]] = min(f[minfactors[x]], prev + 1)
                cur = min(f[minfactors[x]], cur)
                x //= minfactors[x]
            prev = cur
        return prev


# 复写
maxnum = 10 ** 6
p = 2
minfactors = [1] * (maxnum + 1)
while p <= maxnum:
    i = p
    while i * p <= maxnum:
        minfactors[i * p] = p
        i += 1
    p += 1
    while p <= maxnum:
        if minfactors[p] == 1:
            break
        p += 1


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = collections.defaultdict(lambda: float('inf'))
        x = nums[0]
        while True:
            if minfactors[x] == 1:
                f[x] = 1
                break
            f[minfactors[x]] = 1
            x //= minfactors[x]
        prev = 1
        for i in range(1, n):
            cur = float('inf')
            x = nums[i]
            while True:
                if minfactors[x] == 1:
                    f[x] = min(f[x], prev + 1)
                    cur = min(cur, f[x])
                    break
                f[minfactors[x]] = min(f[minfactors[x]], prev + 1)
                cur = min(cur, f[minfactors[x]])
                x//=minfactors[x]
            prev=cur
        return prev


Solution().splitArray([326614, 489921])
