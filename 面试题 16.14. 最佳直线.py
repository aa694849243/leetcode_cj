#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。
#  设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小
# 的直线返回，S[0]相同则选择S[1]值较小的直线返回。
#  示例：
#  输入： [[0,0],[1,1],[1,0],[2,0]]
# 输出： [0,2]
# 解释： 所求直线穿过的3个点的编号为[0,2,3]
#
#  提示：
#
#  2 <= len(Points) <= 300
#  len(Points[i]) = 2
#
#  Related Topics 几何 数组 哈希表 数学
#  👍 16 👎 0

# 必须剪枝
class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        if not points:
            return []
        if len(points) == 1:
            return [0]
        if len(points) == 2:
            return [0, 1]

        ma = 1
        ans = []
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                x1 = complex(*points[i])
                x2 = complex(*points[j])
                v1 = x2 - x1
                cnt = 2
                tmp = [i, j]
                if len(points) - j + 1 <= ma:
                    break
                for k in range(j + 1, len(points)):
                    x3 = complex(*points[k])
                    v2 = x3 - x1
                    if v1.imag * v2.real == v1.real * v2.imag:
                        cnt += 1
                if cnt > ma:
                    ans = tmp
                    ma = cnt
        return ans


Solution().bestLine(
    [[-38935, 27124], [-39837, 19604], [-7086, 42194], [-11571, -23257], [115, -23257], [20229, 5976], [24653, -18488], [11017, 21043],
     [-9353, 16550], [-47076, 15237], [-36686, 42194], [-17704, 1104], [31067, 7368], [-20882, 42194], [-19107, -10597], [-14898, 24506],
     [-20801, 42194], [-52268, 40727], [-14042, 42194], [-23254, 42194], [-30837, -53882], [1402, 801], [-33961, -984], [-6411, 42194],
     [-12210, 22901], [-8213, -19441], [-26939, 20810], [30656, -23257], [-27195, 21649], [-33780, 2717], [23617, 27018], [12266, 3608]])
