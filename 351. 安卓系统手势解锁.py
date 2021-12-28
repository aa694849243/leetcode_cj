#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。用户可以设置一个 “解锁模式” ，通过连接特定序列中的点，形成一系列彼此连接的线
# 段，每个线段的端点都是序列中两个连续的点。如果满足以下两个条件，则 k 点序列是有效的解锁模式：
#
#
#  解锁模式中的所有点 互不相同 。
#  假如模式中两个连续点的线段需要经过其他点，那么要经过的点必须事先出现在序列中（已经经过），不能跨过任何还未被经过的点。
#
#
#
#
#  以下是一些有效和无效解锁模式的示例：
#
#
#
#
#
#  无效手势：[4,1,3,6] ，连接点 1 和点 3 时经过了未被连接过的 2 号点。
#  无效手势：[4,1,9,2] ，连接点 1 和点 9 时经过了未被连接过的 5 号点。
#  有效手势：[2,4,1,3,6] ，连接点 1 和点 3 是有效的，因为虽然它经过了点 2 ，但是点 2 在该手势中之前已经被连过了。
#  有效手势：[6,5,4,1,9,2] ，连接点 1 和点 9 是有效的，因为虽然它经过了按键 5 ，但是点 5 在该手势中之前已经被连过了。
#
#
#  给你两个整数，分别为 m 和 n ，那么请你统计一下有多少种 不同且有效的解锁模式 ，是 至少 需要经过 m 个点，但是 不超过 n 个点的。
#
#  两个解锁模式 不同 需满足：经过的点不同或者经过点的顺序不同。
#
#
#
#  示例 1：
#
#
# 输入：m = 1, n = 1
# 输出：9
#
#
#  示例 2：
#
#
# 输入：m = 1, n = 2
# 输出：65
#
#
#
#
#  提示：
#
#
#  1 <= m, n <= 9
#
#  Related Topics 动态规划 回溯
#  👍 91 👎 0
import functools


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def check(i, path):
            if not path:
                return True
            if i in path:
                return False
            last = path[-1]
            if last == 1:
                if i == 3:
                    return 2 in path
                elif i == 7:
                    return 4 in path
                elif i == 9:
                    return 5 in path
                else:
                    return True
            elif last == 2:
                if i == 8:
                    return 5 in path
                else:
                    return True
            elif last == 3:
                if i == 1:
                    return 2 in path
                elif i == 9:
                    return 6 in path
                elif i == 7:
                    return 5 in path
                else:
                    return True
            elif last == 5:
                return True
            elif last == 4:
                if i == 6:
                    return 5 in path
                else:
                    return True
            elif last == 6:
                if i == 4:
                    return 5 in path
                return True
            elif last == 7:
                if i == 1:
                    return 4 in path
                elif i == 3:
                    return 5 in path
                elif i == 9:
                    return 8 in path
                else:
                    return True
            elif last == 8:
                if i == 2:
                    return 5 in path
                else:
                    return True
            elif last == 9:
                if i == 1:
                    return 5 in path
                elif i == 3:
                    return 6 in path
                elif i == 7:
                    return 8 in path
                else:
                    return True

        self.res = 0
        self.ans = []

        @functools.lru_cache(None)
        def dfs(x, path):
            if x > n:
                return
            for i in range(1, 10):
                if check(i, path):
                    if m <= x <= n:
                        self.ans.append(path+(i,))
                        self.res += 1
                    dfs(x + 1, path + (i,))

        dfs(1, tuple())
        return self.res


Solution().numberOfPatterns(1, 2)
