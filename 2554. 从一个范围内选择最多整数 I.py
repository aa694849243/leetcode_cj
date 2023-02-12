# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 23:51 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        pre = 0
        res = 0
        for num in range(1, n + 1):
            if num in banned:
                continue
            if pre + num > maxSum:
                break
            pre += num
            res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

