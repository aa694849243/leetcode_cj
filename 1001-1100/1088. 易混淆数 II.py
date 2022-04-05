#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 本题我们会将数字旋转 180° 来生成一个新的数字。
#
#  比如 0、1、6、8、9 旋转 180° 以后，我们得到的新数字分别为 0、1、9、8、6。
#
#  2、3、4、5、7 旋转 180° 后，是 无法 得到任何数字的。
#
#  易混淆数（Confusing Number）指的是一个数字在整体旋转 180° 以后，能够得到一个和原来 不同 的数，且新数字的每一位都应该是有效的。（请
# 注意，旋转后得到的新数字可能大于原数字）
#
#  给出正整数 N，请你返回 1 到 N 之间易混淆数字的数量。
#
#
#
#  示例 1：
#
#  输入：20
# 输出：6
# 解释：
# 易混淆数为 [6,9,10,16,18,19]。
# 6 转换为 9
# 9 转换为 6
# 10 转换为 01 也就是 1
# 16 转换为 91
# 18 转换为 81
# 19 转换为 61
#
#
#  示例 2：
#
#  输入：100
# 输出：19
# 解释：
# 易混淆数为 [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100]。
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#
#  Related Topics 数学 回溯
#  👍 27 👎 0


class Solution:
    def confusingNumberII(self, n: int) -> int:
        if n < 6:
            return 0
        elif n < 9:
            return 1
        elif n == 9:
            return 2

        n_str = [*map(int, str(n))]
        leng = len(n_str)
        m = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        less = [0, 1, 2, 2, 2, 2, 2, 3, 3, 4]  # 表示小于位置i的混淆数（0，1，6，8，9）的数量
        res = 5 ** (leng - 1) - 1  # 减去0 ，非顶格位
        res += (less[n_str[0]] - 1) * 5 ** (leng - 1)  # less[n_st[0]]-1最高位不能为0
        if n_str[0] in m:
            for i in range(1, leng):
                res += (less[n_str[i]]) * 5 ** (leng - 1 - i)  # 非最高位可以取0
                if n_str[i] not in m:
                    break
            else:
                res += 1  # 补上顶格数
        for i in range(1, leng):  # 开始减去倒转后完全相同的数字
            if i == 1:  # 减去1，8
                res -= 2
            elif i % 2:
                res -= 3 * 4 * 5 ** (i - 3 >> 1)  # {1，6，8，9}+{0,1,8}
            else:
                res -= 4 * 5 ** (i - 2 >> 1)
        if leng % 2:  # 分奇偶讨论
            res -= (less[n_str[0]] - 1) * 3 * 5 ** (leng - 3 >> 1)
            if n_str[0] not in m:
                return res
            for i in range(1, leng >> 1):
                res -= (less[n_str[i]]) * 3 * 5 ** ((leng - 3 >> 1) - i)
                if n_str[i] not in m:
                    return res
            a = n_str[leng >> 1]
            if not a:  # a==0的情况
                pass
            elif a == 1:
                res -= 1
            elif a < 8:  # 中间数可以为0，1
                res -= 2
                return res
            elif a == 8:
                res -= 2
            else:  # a==9的情况
                res -= 3
                return res
            for i in range((leng >> 1) + 1, leng):
                a, b = n_str[-i - 1], n_str[i]
                if b > m[a]:
                    break
                if b < m[a]:  # 唯一种情况9和<6以及6和<9这两种情况则说明都进行不下去了
                    return res
            return res - 1  # 全部匹配的情况，说明顶格值也匹配，直接剪掉那个顶格值
        else:
            res -= (less[n_str[0]] - 1) * 5 ** (leng - 2 >> 1)
            if n_str[0] not in m:
                return res
            for i in range(1, leng >> 1):
                res -= (less[n_str[i]]) * 5 ** ((leng - 2 >> 1) - i)
                if n_str[i] not in m:
                    return res
            for i in range(leng >> 1, leng):  # 从中间往外扩散，从高往低找唯一一个与前半段顶格值对应的数
                a, b = n_str[-i - 1], n_str[i]
                if b > m[a]:
                    break
                if b < m[a]:
                    return res
            return res - 1


#

# class Solution:
#     def confusingNumberII(self, N: int) -> int:
#         if N < 6:
#             return 0
#         elif N < 9:
#             return 1
#         elif N == 9:
#             return 2
#
#         N = list(map(int, list(str(N))))
#         n = len(N)
#         res = 5 ** (n - 1) - 1  # 计算数位小于n且由reflex中的数作数码的个数
#         less = [0, 1, 2, 2, 2, 2, 2, 3, 3, 4]  # less[i]表示小于i且属于reflex的数的个数
#         reflex = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
#         # 根据N每一位的数码，计算数位等于n且由reflex中的数作数码的个数
#         res += (less[N[0]] - 1) * 5 ** (n - 1)
#         if N[0] in reflex:
#             for i in range(1, n):
#                 res += less[N[i]] * 5 ** (n - i - 1)
#                 if N[i] not in reflex:
#                     break
#             else:
#                 res += 1
#
#         # 计算数位小于n且由reflex中的数作数码的非混淆数
#         for i in range(1, n):
#             if i == 1:
#                 res -= 2
#             elif i & 1:
#                 res -= 12 * 5 ** (i - 3 >> 1)
#             else:
#                 res -= 4 * 5 ** (i - 2 >> 1)
#
#         # 根据n的奇偶性分类讨论
#         if n & 1:
#             res -= 3 * (less[N[0]] - 1) * 5 ** (n - 3 >> 1)
#             if N[0] not in reflex:
#                 return res
#
#             for i in range(1, n >> 1):
#                 res -= 3 * less[N[i]] * 5 ** ((n - 3 >> 1) - i)
#                 if N[i] not in reflex:
#                     return res
#
#             a = N[n >> 1]
#             if not a:
#                 pass
#             elif a == 1:
#                 res -= 1
#             elif a < 8:
#                 res -= 2
#                 return res
#             elif a == 8:
#                 res -= 2
#             elif a == 9:
#                 res -= 3
#                 return res
#
#             for i in range((n >> 1) + 1, n):
#                 a, b = N[-i - 1], N[i]
#                 if b > reflex[a]:
#                     return res - 1
#                 if b < reflex[a]:
#                     return res
#             return res - 1
#         else:
#             res -= (less[N[0]] - 1) * 5 ** (n - 2 >> 1)
#             if N[0] not in reflex:
#                 return res
#
#             for i in range(1, n >> 1):
#                 res -= less[N[i]] * 5 ** ((n >> 1) - i - 1)
#                 if N[i] not in reflex:
#                     return res
#
#             for i in range((n >> 1), n):
#                 a, b = N[-i - 1], N[i]
#                 if b > reflex[a]:
#                     return res - 1
#                 if b < reflex[a]:
#                     return res
#             return res - 1


print(Solution().confusingNumberII(100))
