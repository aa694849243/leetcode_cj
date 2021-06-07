# -*- coding: utf-8 -*-
import collections
from typing import List


# 给定由若干 0 和 1 组成的矩阵 matrix，从中选出任意数量的列并翻转其上的 每个 单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变为 0
# 。
#
#  回经过一些翻转后，行与行之间所有值都相等的最大行数。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：[[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
#
#
#  示例 2：
#
#
# 输入：[[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
#
#
#  示例 3：
#
#
# 输入：[[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。
#
#
#
#  提示：
#
#
#  1 <= matrix.length <= 300
#  1 <= matrix[i].length <= 300
#  所有 matrix[i].length 都相等
#  matrix[i][j] 为 0 或 1
#
#  Related Topics 哈希表
#  👍 35 👎 0

# https://leetcode-cn.com/problems/flip-columns-for-maximum-number-of-equal-rows/solution/1072-an-lie-fan-zhuan-de-dao-zui-da-zhi-deng-xing-/
# 特征模式
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m=collections.defaultdict(int)
        for row in matrix:
            if row[0]==0:
                row=list(map(str,row))
                m[''.join(row)]+=1
            else:
                a=lambda x:str(x^1)
                row=list(map(a,row))
                m[''.join(row)]+=1
        return max(m.values())



