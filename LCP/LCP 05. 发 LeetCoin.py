# -*- coding: utf-8 -*-
import collections
from typing import List


# 力扣决定给一个刷题团队发LeetCoin作为奖励。同时，为了监控给大家发了多少LeetCoin，力扣有时候也会进行查询。
#
#
#
#  该刷题团队的管理模式可以用一棵树表示：
#
#
#  团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）；
#  不存在循环管理的情况，如A管理B，B管理C，C管理A。
#
#
#
#
#  力扣想进行的操作有以下三种：
#
#
#  给团队的一个成员（也可以是负责人）发一定数量的LeetCoin；
#  给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin；
#  查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和。
#
#
#
#
#  输入：
#
#
#  N表示团队成员的个数（编号为1～N，负责人为1）；
#  leadership是大小为(N - 1) * 2的二维数组，其中每个元素[a, b]代表b是a的下属；
#  operations是一个长度为Q的二维数组，代表以时间排序的操作，格式如下：
#
#  operations[i][0] = 1: 代表第一种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetC
# oin的数量；
#  operations[i][0] = 2: 代表第二种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetC
# oin的数量；
#  operations[i][0] = 3: 代表第三种操作，operations[i][1]代表成员的编号；
#
#
#
#
#  输出：
#
#  返回一个数组，数组里是每次查询的返回值（发LeetCoin的操作不需要任何返回值）。由于发的LeetCoin很多，请把每次查询的结果模1e9+7 (100
# 0000007)。
#
#
#
#  示例 1：
#
#  输入：N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations =
#  [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
# 输出：[650, 665]
# 解释：团队的管理关系见下图。
# 第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0;
# 第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15.
#
#
#
#
#
#
#  限制：
#
#
#  1 <= N <= 50000
#  1 <= Q <= 50000
#  operations[i][0] != 3 时，1 <= operations[i][2] <= 5000
#
#  Related Topics 树状数组 线段树 数组
#  👍 42 👎 0

# dfs序+树状数组
class ftree_range:  # 区间修改+区间查询的线段树
    def __init__(self, n):
        self.n = n
        self.d1 = [0] * (n + 1)
        self.d2 = [0] * (n + 1)

    @staticmethod
    def lowbit(i):
        return i & -i

    def add(self, i, dx):
        p = i
        while i <= self.n:
            self.d1[i] += dx
            self.d2[i] += p * dx
            i += self.lowbit(i)

    def range_add(self, l, r, x):
        self.add(l, x)
        self.add(r + 1, -x)

    def ask(self, i):
        ans = 0
        p = i
        while i > 0:
            ans += (p + 1) * self.d1[i] - self.d2[i]
            i -= self.lowbit(i)
        return ans

    def range_ask(self, l, r):
        return self.ask(r) - self.ask(l - 1)


class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for x, y in leadership:
            g[x].append(y)
        time = 1  # 时间戳
        m = {}

        def dfs(node):
            nonlocal time
            l = time
            for nxt in g[node]:
                time += 1
                dfs(nxt)
            m[node] = (l, time)

        dfs(1)
        tree = ftree_range(n)
        ans = []
        for op in operations:
            l, r = m[op[1]]
            if op[0] == 1:  # 单点更新
                tree.range_add(l, l, op[2])
            elif op[0] == 2:
                tree.range_add(l, r, op[2])
            else:
                ans.append(tree.range_ask(l, r) % (10 ** 9 + 7))
        return ans
