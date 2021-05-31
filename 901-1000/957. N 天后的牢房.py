import collections, heapq, itertools
from typing import List


# 8 间牢房排成一排，每间牢房不是有人住就是空着。
#
#  每天，无论牢房是被占用或空置，都会根据以下规则进行更改：
#
#
#  如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
#  否则，它就会被空置。
#
#
#  （请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）
#
#  我们用以下方式描述监狱的当前状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0。
#
#  根据监狱的初始状态，在 N 天后返回监狱的状况（和上述 N 种变化）。
#
#
#
#
#
#
#  示例 1：
#
#  输入：cells = [0,1,0,1,1,0,0,1], N = 7
# 输出：[0,0,1,1,0,0,0,0]
# 解释：
# 下表概述了监狱每天的状况：
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
#
#
#  示例 2：
#
#  输入：cells = [1,0,0,1,0,0,1,0], N = 1000000000
# 输出：[0,0,1,1,1,1,1,0]
#
#
#
#
#  提示：
#
#
#  cells.length == 8
#  cells[i] 的值为 0 或 1
#  1 <= N <= 10^9
#
#  Related Topics 哈希表
#  👍 91 👎 0


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        m = {}
        index = {}
        index[0] = cells
        m[tuple(cells)] = 0
        for i in range(1, n + 1):
            tmp = [0] * 8
            for j in range(1, 7):
                if cells[j - 1] == 0 and cells[j + 1] == 0 or cells[j - 1] == 1 and cells[j + 1] == 1:
                    tmp[j] = 1
                else:
                    tmp[j] = 0
            cells = tmp
            if tuple(cells) in m:
                l = m[tuple(cells)]
                r = i
                break
            m[tuple(cells)] = i
            index[i]=cells
        else:
            return cells
        n -= l
        return index[l+(n % (r-l))]
Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)