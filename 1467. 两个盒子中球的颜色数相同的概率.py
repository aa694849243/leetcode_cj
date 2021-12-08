# -*- coding: utf-8 -*-
# 桌面上有 2n 个颜色不完全相同的球，球上的颜色共有 k 种。给你一个大小为 k 的整数数组 balls ，其中 balls[i] 是颜色为 i 的球的数量
# 。
#
#  所有的球都已经 随机打乱顺序 ，前 n 个球放入第一个盒子，后 n 个球放入另一个盒子（请认真阅读示例 2 的解释部分）。
#
#  注意：这两个盒子是不同的。例如，两个球颜色分别为 a 和 b，盒子分别为 [] 和 ()，那么 [a] (b) 和 [b] (a) 这两种分配方式是不同的
# （请认真阅读示例 1 的解释部分）。
#
#  请计算「两个盒子中球的颜色数相同」的情况的概率。
#
#
#
#  示例 1：
#
#  输入：balls = [1,1]
# 输出：1.00000
# 解释：球平均分配的方式只有两种：
# - 颜色为 1 的球放入第一个盒子，颜色为 2 的球放入第二个盒子
# - 颜色为 2 的球放入第一个盒子，颜色为 1 的球放入第二个盒子
# 这两种分配，两个盒子中球的颜色数都相同。所以概率为 2/2 = 1 。
#
#
#  示例 2：
#
#  输入：balls = [2,1,1]
# 输出：0.66667
# 解释：球的列表为 [1, 1, 2, 3]
# 随机打乱，得到 12 种等概率的不同打乱方案，每种方案概率为 1/12 ：
# [1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1],
# [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
# 然后，我们将前两个球放入第一个盒子，后两个球放入第二个盒子。
# 这 12 种可能的随机打乱方式中的 8 种满足「两个盒子中球的颜色数相同」。
# 概率 = 8/12 = 0.66667
#
#
#  示例 3：
#
#  输入：balls = [1,2,1,2]
# 输出：0.60000
# 解释：球的列表为 [1, 2, 2, 3, 4, 4]。要想显示所有 180 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 108 种情况
# 是比较容易的。
# 概率 = 108 / 180 = 0.6 。
#
#
#  示例 4：
#
#  输入：balls = [3,2,1]
# 输出：0.30000
# 解释：球的列表为 [1, 1, 1, 2, 2, 3]。要想显示所有 60 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 18 种情况是比
# 较容易的。
# 概率 = 18 / 60 = 0.3 。
#
#
#  示例 5：
#
#  输入：balls = [6,6,6,6,6,6]
# 输出：0.90327
#
#
#
#
#  提示：
#
#
#  1 <= balls.length <= 8
#  1 <= balls[i] <= 6
#  sum(balls) 是偶数
#  答案与真实值误差在 10^-5 以内，则被视为正确答案
#
#  Related Topics 数学 动态规划 回溯 组合数学 概率与统计 👍 42 👎 0

import math
from typing import List


# https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/solution/hui-su-jian-zhi-rong-yi-li-jie-by-suibianfahui/
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        m = {}

        def factorial_(num):
            '''返回num!'''
            if num in m:
                return m[num]
            m[num] = math.factorial(num)
            return m[num]

        def calarrange(lst: List[int], num: int) -> int:
            '''
            返回组合为lst的排列数
            :param lst:
            :param nums:
            :return:
            '''
            res = factorial_(num)
            for x in lst:
                res //= factorial_(x)
            return res

        colorsm = len(balls)  # 总颜色
        ballsm = sum(balls)  # 球总数量
        self.res = 0

        def f(c: int, ca: List[int], cb: List[int], sma: int, smb: int) -> None:
            """
            :param c: 总颜色数
            :param ca: a箱子颜色列表,每个格子代表一个颜色，a[i]代表该颜色球的数目
            :param cb: b箱子颜色列表
            :param sma: a箱子球总数
            :param smb: b箱子球总数
            :return:
            边界条件为c==colorsm，此时不再分配，直接比对结果
            """
            if c == colorsm:
                if sma != smb or len(ca) != len(cb):
                    return
                self.res += calarrange(ca, sma) * calarrange(cb, smb)
            else:
                tmp_sm = balls[c]  # 该颜色格子上球总数
                for tmp_a in range(tmp_sm + 1):
                    if tmp_a == 0:
                        f(c + 1, ca, cb + [tmp_sm], sma, smb + tmp_sm)
                    elif tmp_a == tmp_sm:
                        f(c + 1, ca + [tmp_sm], cb, sma + tmp_sm, smb)
                    else:
                        f(c + 1, ca + [tmp_a], cb + [tmp_sm - tmp_a], sma + tmp_a, smb + tmp_sm - tmp_a)

        f(0, [], [], 0, 0)
        return self.res/calarrange(balls,ballsm)
