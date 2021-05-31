# -*- coding: utf-8 -*-
from typing import List


# 在一排多米诺骨牌中，A[i] 和 B[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 ——
# 该平铺的每一半上都有一个数字。）
#
#  我们可以旋转第 i 张多米诺，使得 A[i] 和 B[i] 的值交换。
#
#  返回能使 A 中所有值或者 B 中所有值都相同的最小旋转次数。
#
#  如果无法做到，返回 -1.
#
#
#
#  示例 1：
#
#
#
#  输入：A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# 输出：2
# 解释：
# 图一表示：在我们旋转之前， A 和 B 给出的多米诺牌。
# 如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
#
#
#  示例 2：
#
#  输入：A = [3,5,1,2,3], B = [3,6,3,3,4]
# 输出：-1
# 解释：
# 在这种情况下，不可能旋转多米诺牌使一行的值相等。
#
#
#
#
#  提示：
#
#
#  1 <= A[i], B[i] <= 6
#  2 <= A.length == B.length <= 20000
#
#  Related Topics 贪心算法 数组
#  👍 75 👎 0


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # 第一个不换，第二个换
        a, b = tops[:], bottoms[:]
        first = 0
        flaga, flagb = a[0], b[0]
        for i in range(1, len(tops)):
            if a[i] != flaga:
                first += 1
                a[i], b[i] = b[i], a[i]
                if a[i] != flaga:
                    first = -1
                    break

        a, b = tops[:], bottoms[:]
        second = 0
        for i in range(1, len(tops)):
            if b[i] != flagb:
                second += 1
                a[i], b[i] = b[i], a[i]
                if b[i] != flagb:
                    second = -1
                    break
        a, b = tops[:], bottoms[:]
        a[0], b[0] = b[0], a[0]
        flaga, flagb = a[0], b[0]
        third = 1
        for i in range(1, len(tops)):
            if a[i] != flaga:
                third += 1
                a[i], b[i] = b[i], a[i]
                if a[i] != flaga:
                    third = -1
                    break
        a, b = tops[:], bottoms[:]
        a[0], b[0] = b[0], a[0]
        flagb=b[0]
        fourth = 1
        for i in range(1, len(tops)):
            if b[i] != flagb:
                fourth += 1
                a[i], b[i] = b[i], a[i]
                if b[i] != flagb:
                    fourth = -1
                    break
        li = [i for i in [first, second, third, fourth] if i > -1]
        return min(li) if li else -1
Solution().minDominoRotations([2,2,1,1,1,1], [1,1,1,2,2,2])