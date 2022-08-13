from typing import List


# @solution-sync:begin
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        lst = [*zip(ages, scores)]
        lst.sort()
        scores = [x[1] for x in lst]
        ages = [x[0] for x in lst]
        for i in range(len(ages)):
            tmp_dp = []
            tmp_m = scores[i]
            for j in range(i):
                tmp_dp.append(dp[j])
                if scores[i] >= scores[j] or (scores[j] > scores[i] and ages[i] == ages[j]):
                    tmp_m = max(tmp_m, dp[j] + scores[i])
            tmp_dp.append(tmp_m)
            dp = tmp_dp[:]
        return max(dp)