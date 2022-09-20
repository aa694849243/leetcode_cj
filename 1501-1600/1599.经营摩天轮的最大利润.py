from typing import List


# @solution-sync:begin
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        res = 0
        cnt = 0
        ma = 0
        ma_cnt = -1
        for p in customers:
            wait += p
            if wait >= 4:
                res += 4 * boardingCost - runningCost
                wait -= 4
            else:
                res += wait * boardingCost - runningCost
                wait = 0
            cnt += 1
            if res > ma:
                ma = res
                ma_cnt = cnt
        while wait > 0:
            if wait >= 4:
                res += 4 * boardingCost - runningCost
                wait -= 4
            else:
                res += wait * boardingCost - runningCost
                wait = 0
            cnt += 1
            if res > ma:
                ma = res
                ma_cnt = cnt
        return ma_cnt if res >= 0 else -1


print(Solution().minOperationsMaxProfit([8, 3], 5, 6))
