from typing import List


# 1 记忆化搜索+二分
# 超时

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] > 1:
            return False
        mem = {}
        right = len(stones)

        def bisect(aim, left, right):
            while left < right:
                mid = (left + right) // 2
                if stones[mid] < aim:
                    left = mid + 1
                elif stones[mid] > aim:
                    right = mid
                else:
                    return mid
            return -1

        def dfs(c_location, prejump):
            if c_location == right - 1:
                return True
            for i in (prejump, prejump + 1, prejump - 1):
                if i == 0:
                    continue
                if stones[c_location] + i > stones[-1]:
                    continue
                if stones[c_location] + i in mem:
                    n_location = mem[stones[c_location] + i]
                else:
                    n_location = bisect(stones[c_location] + i, c_location + 1, right)
                    if n_location == -1: continue
                    mem[stones[c_location] + i] = n_location
                if dfs(n_location, i):
                    return True
            return False

        return dfs(1, 1)


Solution().canCross([0,1, 2, 3, 4, 8, 9, 11])
# 2 动态规划
import collections


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mem = collections.defaultdict(set)
        mem[0].add(0)
        for i in stones[1:]:
            mem[i] = set()
        for i in range(len(stones)):
            for jumpsize in mem[stones[i]]:
                for k in [jumpsize - 1, jumpsize, jumpsize + 1]:
                    if k < 1:
                        continue
                    if stones[i] + k == stones[-1]:
                        return True
                    if stones[i] + k in mem:
                        mem[stones[i] + k].add(k)
        return False


Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])
