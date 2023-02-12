# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-01 20:39 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# 二维差分
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff_grad = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff_grad[r1][c1] += 1
            diff_grad[r1][c2 + 1] -= 1
            diff_grad[r2 + 1][c1] -= 1
            diff_grad[r2 + 1][c2 + 1] += 1
        res = []
        cnt, pre = [0] * (n + 1), [0] * (n + 1)
        for r in range(n):
            for c in range(n):
                cnt[c + 1] = cnt[c] + diff_grad[r][c] + pre[c + 1] - pre[c]
            pre = cnt[:]
            res.append(cnt[1:])
        return res
# leetcode submit region end(Prohibit modification and deletion)

