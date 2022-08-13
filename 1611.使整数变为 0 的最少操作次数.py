#格雷码
import functools

# https://leetcode-cn.com/problems/minimum-one-bit-operations-to-make-integers-zero/solution/xiang-jie-ge-lei-ma-by-simpleson/
class Solution:
    @functools.lru_cache(None)
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        return n^self.minimumOneBitOperations(n>>1)



print(Solution().minimumOneBitOperations(9))
