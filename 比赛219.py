class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1:
            cnt += n // 2
            if n % 2:
                n = n // 2 + 1
            else:
                n //= 2
        return cnt


Solution().numberOfMatches(14)


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(max(set(n))), 1)


from typing import List


class Solution:
    def __init__(self):
        self.ans = 0

    def stoneGameVII(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return 0

        def cal(x, i, j, flag):
            if flag == 0:
                x = precum[j] - precum[i]

                return x, i + 1, j
            else:
                x += precum[j - 1] - precum[i - 1]
                return x, i, j - 1

        def cal2(x,i, j):
            x_, i_, j_ = cal(0, i, j, 0)
            x += x_
            cal(0, i, j, 1)

        precum = [stones[0]]
        for i in range(1, len(stones)):
            precum.append(precum[-1] + stones[i])
        cal2(0, 0, 0, len(stones) - 1)
        return self.ans


Solution().stoneGameVII([5, 3, 1, 4, 2])
