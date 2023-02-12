# -*- coding: utf-8 -*-
from functools import lru_cache


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot_num, fac_num = len(robot), len(factory)
        robot.sort()
        factory.sort()

        @lru_cache(None)
        def f(i, j):  # i代表工厂pos，j代表该工厂起始修理的robot的pos
            if j >= robot_num: return 0
            if i == fac_num - 1:
                if robot_num - j > factory[i][1]: return inf
                return sum(abs(robot[p] - factory[i][0]) for p in range(j, robot_num))
            res = f(i + 1, j)  # i工厂不修理任何机器的情况
            tmp = 0
            for k in range(1, factory[i][1] + 1):
                if j + k >= robot_num:
                    break
                tmp += abs(robot[j + k - 1] - factory[i][0])
                res = min(res, tmp + f(i + 1, j + k))
            return res

        return f(0, 0)
