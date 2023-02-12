# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 20:52 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        if not matrix or not matrix[0]:
            return 0
        R, C = len(matrix), len(matrix[0])
        f = [[0] * C for _ in range(R)]
        ans = 0
        for r in range(R):
            cnt = 0
            for c in range(C):
                if matrix[r][c] == '0':
                    cnt = 0
                else:
                    cnt += 1
                f[r][c] = cnt
                ans = max(ans, cnt)
        for c in range(C):
            stk = []
            right = [R] * R
            for r in range(R):
                while stk and f[stk[-1]][c] > f[r][c]:
                    p = stk.pop()
                    right[p] = r
                stk.append(r)
            stk = []
            left = [-1] * R
            for r in range(R - 1, -1, -1):
                while stk and f[stk[-1]][c] > f[r][c]:
                    p = stk.pop()
                    left[p] = r
                stk.append(r)
            for r in range(R):
                ans = max(ans, (right[r] - left[r] - 1) * f[r][c])

        return ans
# leetcode submit region end(Prohibit modification and deletion)

