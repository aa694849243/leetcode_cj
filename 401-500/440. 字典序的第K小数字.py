# 给定整数 n 和 k，返回 [1, n] 中字典序第 k 小的数字。
#
#
#
#  示例 1:
#
#
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
#
#
#  示例 2:
#
#
# 输入: n = 1, k = 1
# 输出: 1
#
#
#
#
#  提示:
#
#
#  1 <= k <= n <= 10⁹
#
#
#  Related Topics 字典树
#  👍 573 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calc_step(cur):
            first, last = cur*10, cur*10+9
            step = 1
            while first <= n:
                step += min(last, n) - first + 1
                first, last = first * 10, last * 10+9
            return step

        k -= 1
        cur = 1
        while k > 0:
            step = calc_step(cur)
            if k - step >= 0:
                k -= step
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().findKthNumber(1000, 1000))
