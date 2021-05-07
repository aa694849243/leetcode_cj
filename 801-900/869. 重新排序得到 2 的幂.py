# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
#  如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
#
#
#
#
#
#
#  示例 1：
#
#  输入：1
# 输出：true
#
#
#  示例 2：
#
#  输入：10
# 输出：false
#
#
#  示例 3：
#
#  输入：16
# 输出：true
#
#
#  示例 4：
#
#  输入：24
# 输出：false
#
#
#  示例 5：
#
#  输入：46
# 输出：true
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#
#  Related Topics 数学
#  👍 40 👎 0
import collections
import itertools


# itertools.permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def is2power(n):
            return n & (-n) == n

        return any(is2power(int(''.join(cand))) for cand in itertools.permutations(str(n)) if cand[0] != '0')


# 2计数
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        return any(count == collections.Counter(str(1 << a)) for a in range(31))
