# -*- coding: utf-8 -*-
from typing import List


# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
#
#  学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试
# 且无法作弊的最大学生人数。
#
#  学生必须坐在状况良好的座位上。
#
#
#
#  示例 1：
#
#
#
#  输入：seats = [["#",".","#","#",".","#"],
#               [".","#","#","#","#","."],
#               ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
#
#
#  示例 2：
#
#  输入：seats = [[".","#"],
#               ["#","#"],
#               ["#","."],
#               ["#","#"],
#               [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
#
#
#  示例 3：
#
#  输入：seats = [["#",".",".",".","#"],
#               [".","#",".","#","."],
#               [".",".","#",".","."],
#               [".","#",".","#","."],
#               ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
#
#
#
#
#  提示：
#
#
#  seats 只包含字符 '.' 和'#'
#  m == seats.length
#  n == seats[i].length
#  1 <= m <= 8
#  1 <= n <= 8
#
#  Related Topics 位运算 数组 动态规划 状态压缩 矩阵
#  👍 114 👎 0


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])
        dp = [0] * (2 ** C)
        leng = 2 ** C
        numseats = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                numseats[r][c] = '0' if seats[r][c] == '#' else '1'
        m={}
        def judge(num):
            if num in m:
                return m[num]
            s=str(bin(num))[2:]
            for i in range(len(s)):
                if i-1>=0 and s[i]==s[i-1]=='1' or i+1<len(s) and s[i]==s[i+1]=='1':
                    return False
            m[num]=True
            return True


        for r in range(R):
            row = numseats[r].copy()
            mask = int(''.join(row), 2)
            ndp = [0] * leng
            for num in range(leng):
                if num & mask == num and judge(num):
                    cnt = str(bin(num)).count('1')
                    for pre in range(leng):
                        if not (num << 1) & pre and not (num >> 1) & pre:
                            ndp[num] = max(ndp[num], dp[pre] + cnt)
            dp = ndp
        return max(dp)
Solution().maxStudents([[".","#","#","."],[".",".",".","#"],[".",".",".","."],["#",".","#","#"]])