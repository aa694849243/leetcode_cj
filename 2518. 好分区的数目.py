# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-30 23:20 
# ide： PyCharm
# https://leetcode.cn/problems/number-of-great-partitions/solution/ni-xiang-si-wei-01-bei-bao-fang-an-shu-p-v47x/
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0
        f = [0] * k
        f[0] = 1
        mod = 10 ** 9 + 7
        for num in nums:
            for j in range(k - 1, num - 1, -1):
                f[j] = (f[j] + f[j - num]) % mod
        return (pow(2, len(nums), mod) - sum(f)*2) % mod
# leetcode submit region end(Prohibit modification and deletion)
