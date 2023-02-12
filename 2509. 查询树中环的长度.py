# -*- coding: utf-8 -*-
# datetime： 2023-01-29 23:26
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/cycle-length-queries-in-a-tree/solution/zui-jin-gong-gong-zu-xian-pythonjavacgo-v8ata/
# 完全二叉数和二进制
# class Solution:
#     def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         res = [0] * len(queries)
#         for i, (a, b) in enumerate(queries):
#             ans = 1
#             while a != b:
#                 if a > b:
#                     a >>= 1
#                 else:
#                     b >>= 1
#                 ans += 1
#             res[i] = ans
#         return res
#

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a < b:
                a, b = b, a
            d = a.bit_length() - b.bit_length()
            ans = d + 1 + (b ^ (a >> d)).bit_length() * 2
            res[i] = ans
        return res
# leetcode submit region end(Prohibit modification and deletion)

