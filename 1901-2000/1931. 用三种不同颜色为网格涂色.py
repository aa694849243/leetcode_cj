# 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
#
#
#  涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 10⁹ + 7 取余 的结果。
#
#
#
#  示例 1：
#
#
# 输入：m = 1, n = 1
# 输出：3
# 解释：如上图所示，存在三种可能的涂色方案。
#
#
#  示例 2：
#
#
# 输入：m = 1, n = 2
# 输出：6
# 解释：如上图所示，存在六种可能的涂色方案。
#
#
#  示例 3：
#
#
# 输入：m = 5, n = 5
# 输出：580986
#
#
#
#
#  提示：
#
#
#  1 <= m <= 5
#  1 <= n <= 1000
#
#
#  Related Topics 动态规划 👍 37 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        valid = {}
        for mask in range(3 ** m):
            color = ''
            tmp_mask = mask
            for _ in range(m):
                color += str(tmp_mask % 3)
                tmp_mask //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color
        adjacement = collections.defaultdict(list)
        for mask1 in valid:
            for mask2 in valid:
                if any(valid[mask1][i] == valid[mask2][i] for i in range(m)):
                    continue
                adjacement[mask1].append(mask2)
        dp = [int(i in valid) for i in range(3 ** m)]
        for i in range(1, n):
            tmp_dp = [0] * (3 ** m)
            for mask1 in valid:
                for mask2 in adjacement[mask1]:
                    tmp_dp[mask1] += dp[mask2]
                    tmp_dp[mask1] %= mod
            dp = tmp_dp
        return sum(dp) % mod


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().colorTheGrid(5, 5))
