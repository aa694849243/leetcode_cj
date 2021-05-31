# -*- coding: utf-8 -*-
from typing import List


# 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0
# 。
#
#  返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。
#
#
#
#  示例 1：
#
#
# 输入：A = [0,1,0], K = 1
# 输出：2
# 解释：先翻转 A[0]，然后翻转 A[2]。
#
#
#  示例 2：
#
#
# 输入：A = [1,1,0], K = 2
# 输出：-1
# 解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
#
#
#  示例 3：
#
#
# 输入：A = [0,0,0,1,0,1,1,0], K = 3
# 输出：3
# 解释：
# 翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
# 翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
# 翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 30000
#  1 <= K <= A.length
#
#  Related Topics 贪心算法 Sliding Window
#  👍 198 👎 0

# 差分
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        diff = [nums[0]]
        for i, num in enumerate(nums[1:], 1):  # 差分数组
            diff.append(num - nums[i - 1])
        cum = 0
        ans = 0
        for i, num in enumerate(nums):
            cum += diff[i]
            if cum % 2 == 0:
                cum += 1
                ans += 1
                if i + k - 1 >= len(nums):  # 翻转的格子不够
                    return -1
                elif i + k == len(nums):  # 翻转的格子刚好
                    continue
                diff[i + k] -= 1
        return ans


# 利用异或
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        diff = [nums[0]]
        for i, num in enumerate(nums[1:], 1):  # 差分数组
            diff.append((num - nums[i - 1]) % 2)
        cum = 0
        ans = 0
        for i, num in enumerate(nums):
            cum ^= diff[i]  # 模二下的加减法与异或等价
            if cum == 0:
                cum ^= 1
                ans += 1
                if i + k == len(nums):
                    continue
                elif i + k > len(nums):
                    return -1
                else:
                    diff[i + k] ^= 1
        return ans


# 3 原数组标记 O(1)空间复杂度
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        cum = 0
        ans = 0
        for i, num in enumerate(nums):
            if i - k >= 0 and nums[i - k] > 1:  # 左端点异常
                cum ^= 1
                nums[i - k] -= 2
            if cum == num:  # 前方翻转次数累计和如果等于num，相当于1进行了奇数次翻转，0进行了偶数次翻转
                ans += 1  # 每一个翻转只和前一个（前面的累积翻转状态）和左端点是否翻转有关
                cum^=1
                if i + k == len(nums):
                    continue
                elif i + k > len(nums):
                    return -1
                else:
                    nums[i]+=2
        return ans


Solution().minKBitFlips([0,0,0,1,0,1,1,0], 3)
