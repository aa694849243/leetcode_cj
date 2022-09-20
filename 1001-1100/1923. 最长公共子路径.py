# 一个国家由 n 个编号为 0 到 n - 1 的城市组成。在这个国家里，每两个 城市之间都有一条道路连接。
#
#  总共有 m 个编号为 0 到 m - 1 的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。每条路径都由一个整数数组表示，每个整数数组表示一个朋
# 友按顺序访问过的城市序列。同一个城市在一条路径中可能 重复 出现，但同一个城市在一条路径中不会连续出现。
#
#  给你一个整数 n 和二维数组 paths ，其中 paths[i] 是一个整数数组，表示第 i 个朋友走过的路径，请你返回 每一个 朋友都走过的 最长公共
# 子路径 的长度，如果不存在公共子路径，请你返回 0 。
#
#  一个 子路径 指的是一条路径中连续的城市序列。
#
#
#
#  示例 1：
#
#
# 输入：n = 5, paths = [[0,1,2,3,4],
#                      [2,3,4],
#                      [4,0,1,2,3]]
# 输出：2
# 解释：最长公共子路径为 [2,3] 。
#
#
#  示例 2：
#
#
# 输入：n = 3, paths = [[0],[1],[2]]
# 输出：0
# 解释：三条路径没有公共子路径。
#
#
#  示例 3：
#
#
# 输入：n = 5, paths = [[0,1,2,3,4],
#                      [4,3,2,1,0]]
# 输出：1
# 解释：最长公共子路径为 [0]，[1]，[2]，[3] 和 [4] 。它们长度都为 1 。
#
#
#
#  提示：
#
#
#  1 <= n <= 10⁵
#  m == paths.length
#  2 <= m <= 10⁵
#  sum(paths[i].length) <= 10⁵
#  0 <= paths[i][j] < n
#  paths[i] 中同一个城市不会连续重复出现。
#
#
#  Related Topics 数组 二分查找 后缀数组 哈希函数 滚动哈希 👍 36 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        mod = 10 ** 18 + 13
        base = random.randint(10**6, 10**7)

        def rabinkarp(s, size):
            mult = pow(base, size - 1, mod)
            m = set()
            hash = 0
            for i in range(size):
                hash = (hash * base + s[i]) % mod
            m.add(hash)
            for i in range(size, len(s)):
                hash = ((hash - s[i - size] * mult) * base + s[i]) % mod
                m.add(hash)
            return m

        l, r = 0, min(len(p) for p in paths) + 1
        while l < r:
            mid = (l + r) // 2
            if mid == 0:
                break
            m = rabinkarp(paths[0], mid)
            for i in range(1, len(paths)):
                m &= rabinkarp(paths[i], mid)
                if not m:
                    break
            if m:
                l = mid + 1
            else:
                r = mid
        return l - 1 if l > 0 else 0

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().longestCommonSubpath(5, [[0, 1, 2, 3, 4, 3, 4]]))