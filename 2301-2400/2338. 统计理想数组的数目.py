# -*- coding: utf-8 -*-
# 给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。
#
#  对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：
#
#
#  每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。
#  每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。
#
#
#  返回长度为 n 的 不同 理想数组的数目。由于答案可能很大，返回对 10⁹ + 7 取余的结果。
#
#
#
#  示例 1：
#
#  输入：n = 2, maxValue = 5
# 输出：10
# 解释：存在以下理想数组：
# - 以 1 开头的数组（5 个）：[1,1]、[1,2]、[1,3]、[1,4]、[1,5]
# - 以 2 开头的数组（2 个）：[2,2]、[2,4]
# - 以 3 开头的数组（1 个）：[3,3]
# - 以 4 开头的数组（1 个）：[4,4]
# - 以 5 开头的数组（1 个）：[5,5]
# 共计 5 + 2 + 1 + 1 + 1 = 10 个不同理想数组。
#
#
#  示例 2：
#
#  输入：n = 5, maxValue = 3
# 输出：11
# 解释：存在以下理想数组：
# - 以 1 开头的数组（9 个）：
#    - 不含其他不同值（1 个）：[1,1,1,1,1]
#    - 含一个不同值 2（4 个）：[1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
#    - 含一个不同值 3（4 个）：[1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
# - 以 2 开头的数组（1 个）：[2,2,2,2,2]
# - 以 3 开头的数组（1 个）：[3,3,3,3,3]
# 共计 9 + 1 + 1 = 11 个不同理想数组。
#
#
#
#
#  提示：
#
#
#  2 <= n <= 10⁴
#  1 <= maxValue <= 10⁴
#
#
#  Related Topics 数学 动态规划 组合数学 数论
#  👍 45 👎 0
import collections
import math


# leetcode submit region begin(Prohibit modification and deletion)
def get_factors(num):  # 分解质因数
    C = collections.Counter()
    p = 2
    while p * p <= num:
        while num % p == 0:
            C[p] += 1
            num //= p
        p += 1
    if num > 1:
        C[num] += 1
    return C


m = {}
for num in range(2, 10 ** 4 + 1):
    m[num] = get_factors(num)


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10 ** 9 + 7
        ans = 1  #全1的情况
        for num in range(2, maxValue + 1):
            mul = 1
            for k, v in m[num].items():
                mul *= math.comb(n + v - 1, n - 1)
                mul %= mod
            ans += mul
        ans %= mod
        return ans
# leetcode submit region end(Prohibit modification and deletion)
from typing import List
print(Solution().idealArrays(2, 5))