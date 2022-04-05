#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 target 和一个数组 initial ，initial 数组与 target 数组有同样的维度，且一开始全部为 0 。
#
#  请你返回从 initial 得到 target 的最少操作次数，每次操作需遵循以下规则：
#
#
#  在 initial 中选择 任意 子数组，并将子数组中每个元素增加 1 。
#
#
#  答案保证在 32 位有符号整数以内。
#
#
#
#  示例 1：
#
#  输入：target = [1,2,3,2,1]
# 输出：3
# 解释：我们需要至少 3 次操作从 intial 数组得到 target 数组。
# [0,0,0,0,0] 将下标为 0 到 4 的元素（包含二者）加 1 。
# [1,1,1,1,1] 将下标为 1 到 3 的元素（包含二者）加 1 。
# [1,2,2,2,1] 将下表为 2 的元素增加 1 。
# [1,2,3,2,1] 得到了目标数组。
#
#
#  示例 2：
#
#  输入：target = [3,1,1,2]
# 输出：4
# 解释：(initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (tar
# get) 。
#
#
#  示例 3：
#
#  输入：target = [3,1,5,4,2]
# 输出：7
# 解释：(initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1]
#                                   -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2]
#  -> [3,1,5,4,2] (target)。
#
#
#  示例 4：
#
#  输入：target = [1,1,1,1]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= target.length <= 10^5
#  1 <= target[i] <= 10^5
#
#  Related Topics 栈 贪心 数组 动态规划 单调栈
#  👍 45 👎 0

# https://leetcode-cn.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solution/xing-cheng-mu-biao-shu-zu-de-zi-shu-zu-zui-shao-ze/
# 差分数组
# 由于是正数数组，所以差分和一定大于0
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        difs = [target[0]]
        for i in range(1, len(target)):
            difs.append(target[i] - target[i - 1])
        res = 0
        for dif in difs:  # 差分数组只改变两个数，差分头和差分尾，差分尾为数组最后一个元素时变成黑洞
            res += max(dif, 0) # 当差分数为负数时，一定有匹配的差分头大于0，那么差分头-1，该差分数+1可以平推到0，而前面的差分头反正也要平推到0，所以碰到差分数为负数时，直接跳过就好了
        return res
