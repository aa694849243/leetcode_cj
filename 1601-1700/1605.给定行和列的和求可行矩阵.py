from typing import List


# @solution-sync:begin
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R, C = len(rowSum), len(colSum)
        res = [[0] * C for _ in range(R)]
        res[0] = colSum[:]
        sum_ = sum(rowSum)
        for i in range(1, R):
            x = rowSum[i - 1]
            delta = sum_ - x
            sum_ = delta
            for j in range(C):
                if res[i - 1][j] <= delta:
                    res[i][j] = res[i - 1][j]
                    delta -= res[i - 1][j]
                    res[i - 1][j] = 0
                else:
                    res[i][j] = delta
                    res[i-1][j] -= delta
                    delta = 0
                if delta == 0:
                    break
        return res


print(Solution().restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]))
