# -*- coding: utf-8 -*-
# datetime： 2023-02-02 23:41
# ide： PyCharm
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/count-increasing-quadruplets/solution/you-ji-qiao-de-mei-ju-yu-chu-li-pythonja-exja/
# greater数组 less数组的写法
# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         n = len(nums)
#         greater = [0] * n
#         greater[-1] = [0] * (n + 1)
#         for k in range(n - 2, 0, -1):  # i,j,k,l 。k至少为2
#             greater[k] = greater[k + 1][:]
#             for x in range(nums[k + 1] - 1, 0, -1):  # 比当前数大的个数，由于最小的数是0，则到1为止
#                 greater[k][x] += 1
#         ans = 0
#         for j in range(1, n - 2):
#             for k in range(j + 1, n - 1):
#                 if nums[j] > nums[k]:
#                     x = nums[k]
#                     g_nums_j = greater[k][nums[j]]  # 比x大的个数
#                     less_x = x - (n - 1 - j - greater[j][x])  # 比x小的个数,x在j右侧，全排列，所以比x小的个数是x-1-(n-1-j-gx)
#                     ans += g_nums_j * less_x
#         return ans


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        greater = [0] * n
        greater[-1] = [0] * (n + 1)
        for k in range(n - 2, 0, -1):  # i,j,k,l 。k至少为2
            greater[k] = greater[k + 1][:]
            for x in range(nums[k + 1] - 1, 0, -1):  # 比当前数大的个数，由于最小的数是0，则到1为止
                greater[k][x] += 1
        ans = 0
        less = [0] * (n + 1)
        for j in range(1, n - 2):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    g_nums_j = greater[k][nums[j]]  # 比x大的个数
                    less_x = less[nums[k]]  # 比x小的个数,x在j右侧，全排列，所以比x小的个数是x-1-(n-1-j-gx)
                    ans += g_nums_j * less_x
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().countQuadruplets([1, 3, 2, 4, 5])
)

