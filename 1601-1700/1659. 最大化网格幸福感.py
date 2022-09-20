import collections, heapq, itertools
import functools
from typing import List


# 给你四个整数 m、n、introvertsCount 和 extrovertsCount 。有一个 m x n 网格，和两种类型的人：内向的人和外向的人。总共有 introvertsCount 个内向的人和 extrovertsCount 个外向的人。
#
# 请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，不必 让所有人都生活在网格中。
#
# 每个人的 幸福感 计算如下：
#
# 内向的人 开始 时有 120 个幸福感，但每存在一个邻居（内向的或外向的）他都会 失去  30 个幸福感。
# 外向的人 开始 时有 40 个幸福感，每存在一个邻居（内向的或外向的）他都会 得到  20 个幸福感。
# 邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。
#
# 网格幸福感 是每个人幸福感的 总和 。 返回 最大可能的网格幸福感 。
#
#  
#
# 示例 1：
#
#
# 输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# 输出：240
# 解释：假设网格坐标 (row, column) 从 1 开始编号。
# 将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
# - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
# - 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
# - 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
# 网格幸福感为：120 + 60 + 60 = 240
# 上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。
# 示例 2：
#
# 输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# 输出：260
# 解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
# - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
# - 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
# - 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
# 网格幸福感为 90 + 80 + 90 = 260
# 示例 3：
#
# 输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# 输出：240
#  
#
# 提示：
#
# 1 <= m, n <= 5
# 0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximize-grid-happiness
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode.cn/problems/maximize-grid-happiness/solution/zui-da-hua-wang-ge-xing-fu-gan-by-zerotrac2/
# 轮廓线dp
# 3进制 三进制
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def calc(x, y):
            if x == 0 or y == 0:
                return 0
            if x == 1 and y == 1:  # 内向的人
                return -60
            if x == 2 and y == 2:  # 外向的人
                return 40
            return -10

        n3 = 3 ** n
        highest = n3 // 3
        next_status = {}  # 下一个状态
        mask_status = {}  # 当前数字状态对应的三进制列表
        for mask in range(n3):
            bits = []
            tmp_mask = mask
            for i in range(n):
                bits.append(mask % 3)
                mask //= 3
            mask_status[tmp_mask] = bits[::-1]  # 0号位为最低位
            next_status[tmp_mask] = [
                tmp_mask % highest * 3,
                tmp_mask % highest * 3 + 1,
                tmp_mask % highest * 3 + 2
            ]

        @functools.lru_cache(None)
        def f(pos, status, nx, wx):
            if pos == n * m or nx + wx == 0:
                return 0
            x, y = divmod(pos, n)
            ans = f(pos + 1, next_status[status][0], nx, wx)
            if nx > 0:
                tmp = 120 + calc(1, mask_status[status][0]) \
                      + (0 if y == 0 else calc(1, mask_status[status][n - 1])) \
                      + f(pos + 1, next_status[status][1], nx - 1, wx)
                ans = max(ans, tmp)
            if wx > 0:
                tmp = 40 + calc(2, mask_status[status][0]) \
                      + (0 if y == 0 else calc(2, mask_status[status][n - 1])) \
                      + f(pos + 1, next_status[status][2], nx, wx - 1)
                ans = max(ans, tmp)
            return ans

        return f(0, 0, introvertsCount, extrovertsCount)


print(Solution().getMaxGridHappiness(2, 3, 1, 2))
