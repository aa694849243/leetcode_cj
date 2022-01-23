# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect
# 新一轮的「力扣杯」编程大赛即将启动，为了动态显示参赛者的得分数据，需要设计一个排行榜 Leaderboard。
#
#  请你帮忙来设计这个 Leaderboard 类，使得它有如下 3 个函数：
#
#
#  addScore(playerId, score)：
#
#
#  假如参赛者已经在排行榜上，就给他的当前得分增加 score 点分值并更新排行。
#  假如该参赛者不在排行榜上，就把他添加到榜单上，并且将分数设置为 score。
#
#
#  top(K)：返回前 K 名参赛者的 得分总和。
#  reset(playerId)：将指定参赛者的成绩清零（换句话说，将其从排行榜中删除）。题目保证在调用此函数前，该参赛者已有成绩，并且在榜单上。
#
#
#  请注意，在初始状态下，排行榜是空的。
#
#
#
#  示例 1：
#
#
# 输入：
# ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top",
# "reset","reset","addScore","top"]
# [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
# 输出：
# [null,null,null,null,null,null,73,null,null,null,141]
#
# 解释：
# Leaderboard leaderboard = new Leaderboard ();
# leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
# leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
# leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
# leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
# leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5
# ,4]];
# leaderboard.top(1);           // returns 73;
# leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
# leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
# leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
# leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
#
#
#
#
#  提示：
#
#
#  1 <= playerId, K <= 10000
#  题目保证 K 小于或等于当前参赛者的数量
#  1 <= score <= 100
#  最多进行 1000 次函数调用
#
#  Related Topics 设计 哈希表 排序 👍 31 👎 0

from sortedcontainers import SortedList


class Leaderboard:

    def __init__(self):
        self.m = {}
        self.li = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.m or self.m[playerId]==0:
            self.m[playerId] = score
            self.li.add(score)
        else:
            old = self.m[playerId]
            self.li.remove(old)
            self.m[playerId] += score
            self.li.add(self.m[playerId])

    def top(self, K: int) -> int:
        res = 0
        for i in range(1, K + 1):
            if i > len(self.li):
                break
            res += self.li[-i]
        return res

    def reset(self, playerId: int) -> None:
        self.li.remove(self.m[playerId])
        self.m[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
