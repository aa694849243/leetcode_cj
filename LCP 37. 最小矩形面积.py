# -*- coding: utf-8 -*-
import collections
from typing import List


# 二维平面上有 $N$ 条直线，形式为 `y = kx + b`，其中 `k`、`b`为整数 且 `k > 0`。所有直线以 `[k,b]` 的形式存于二维数
# 组 `lines` 中，不存在重合的两条直线。两两直线之间可能存在一个交点，最多会有 $C_N^2$ 个交点。我们用一个平行于坐标轴的矩形覆盖所有的交点，请问这
# 个矩形最小面积是多少。若直线之间无交点、仅有一个交点或所有交点均在同一条平行坐标轴的直线上，则返回0。
#
# 注意：返回结果是浮点数，与标准答案 **绝对误差或相对误差** 在 10^-4 以内的结果都被视为正确结果
#
#
# **示例 1：**
# > 输入：`lines = [[2,3],[3,0],[4,1]]`
# >
# > 输出：`48.00000`
# >
# > 解释：三条直线的三个交点为 (3, 9) (1, 5) 和 (-1, -3)。最小覆盖矩形左下角为 (-1, -3) 右上角为 (3,9)，面积为 48
#
#
#
# **示例 2：**
# > 输入：`lines = [[1,1],[2,3]]`
# >
# > 输出：`0.00000`
# >
# > 解释：仅有一个交点 (-2，-1）
#
#
# **限制：**
# + `1 <= lines.length <= 10^5 且 lines[i].length == 2`
# + `1 <= lines[0] <= 10000`
# + `-10000 <= lines[1] <= 10000`
# + `与标准答案绝对误差或相对误差在 10^-4 以内的结果都被视为正确结果` Related Topics 贪心 几何 数组 数学 组合数学 排序
#  👍 11 👎 0

# https://leetcode-cn.com/problems/zui-xiao-ju-xing-mian-ji/solution/xiang-lin-liang-lie-jue-dui-bu-hui-shu-d-s95z/

class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
        from fractions import Fraction
        Xmin, Ymin = float('inf'), float('inf')
        Xmax, Ymax = float('-inf'), float('-inf')
        mxk = collections.defaultdict(list)
        myk = collections.defaultdict(list)
        for k, b in lines:
            mxk[k].append(b)
            if k != 0:
                myk[Fraction(1, k)].append(Fraction(b, k))
            else:
                Ymin = min(b, Ymin)
                Ymax = max(b, Ymax)
        lix, liy = sorted(mxk), sorted(myk)
        for i in range(1, len(lix)):
            kj, ki = lix[i - 1], lix[i]
            bj_max, bj_min = max(mxk[kj]), min(mxk[kj])
            bi_max, bi_min = max(mxk[ki]), min(mxk[ki])
            x1, x2 = -(bi_min - bj_max) / (ki - kj), -(bi_max - bj_min) / (ki - kj)
            Xmax, Xmin = max(x1, x2, Xmax), min(x1, x2, Xmin)
        for i in range(1, len(liy)):
            kj, ki = liy[i - 1], liy[i]
            bj_max, bj_min = max(myk[kj]), min(myk[kj])
            bi_max, bi_min = max(myk[ki]), min(myk[ki])
            y1, y2 = (bi_min - bj_max) / (ki - kj), (bi_max - bj_min) / (ki - kj)
            Ymax, Ymin = max(y1, y2, Ymax), min(y1, y2, Ymin)
        ans=(Ymax-Ymin)*(Xmax-Xmin)
        return ans if ans!=float('inf') else 0
Solution().minRecSize(lines = [[1,1],[2,3]])