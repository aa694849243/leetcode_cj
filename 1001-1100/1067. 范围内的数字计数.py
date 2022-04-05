#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个在 0 到 9 之间的整数 d，和两个正整数 low 和 high 分别作为上下界。返回 d 在 low 和 high 之间的整数中出现的次数，包括
# 边界 low 和 high。
#
#
#
#  示例 1：
#
#  输入：d = 1, low = 1, high = 13
# 输出：6
# 解释：
# 数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。
#
#
#  示例 2：
#
#  输入：d = 3, low = 100, high = 250
# 输出：35
# 解释：
# 数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。
#
#
#
#
#  提示：
#
#
#  0 <= d <= 9
#  1 <= low <= high <= 2×10^8
#
#  Related Topics 数学 动态规划
#  👍 20 👎 0

# 标准数位dp
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        edge = str(low).count(str(d))
        if low == high:
            return edge
        return edge + self.cal(high, d) - self.cal(low, d)

    def cal(self, num, d) -> int:
        res = 0
        num = str(num)
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) == d:
                part1 = int(num[:i]) * 10 ** (len(num) - i - 1) if i != 0 else 0
                part2 = 1 + int(num[i + 1:]) if i != len(num) - 1 else 1
                res += part1 + part2
            elif int(num[i]) > d:
                part1 = (1 + int(num[:i])) * 10 ** (len(num) - i - 1) if i != 0 else 10 ** (len(num) - i - 1)
                res += part1
            else:
                part1 = int(num[:i]) * 10 ** (len(num) - i - 1) if i != 0 else 0
                res += part1
        if d == 0:
            for i in range(1, len(num)):
                res -= 10 ** i
        return res


from collections import Counter


# class Solution:
#     def digitsCount(self, d, low, high):
#         edge = Counter(str(low))[str(d)]
#         if low == high:
#             return edge
#         ans = edge + self.count(high, d) - self.count(low, d)
#         return ans
#
#     def count(self, limit, d):
#         num_str = str(limit)
#         res = 0
#         for i in range(len(num_str) - 1, -1, -1):
#             if d == int(num_str[i]):
#                 part1 = int(num_str[:i]) * pow(10, len(num_str) - (i + 1)) if i != 0 else 0
#                 part2 = 1 * (1 + int(num_str[i + 1:])) if i != len(num_str) - 1 else 1
#                 res = res + part1 + part2
#             elif d < int(num_str[i]):
#                 prev = 1 + int(num_str[:i]) if i != 0 else 1
#                 part1 = prev * pow(10, len(num_str) - (i + 1))
#                 res = res + part1
#             else:
#                 part1 = int(num_str[:i]) * pow(10, len(num_str) - (i + 1)) if i != 0 else 0
#                 res = res + part1
#         if d == 0:
#             for i in range(1, len(num_str)):
#                 res = res - pow(10, i)
#         return res


Solution().digitsCount(0, 1080, 2160)
