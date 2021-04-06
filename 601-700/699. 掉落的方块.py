'''在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。

第 i 个掉落的方块（positions[i] = (left, side_length)）是正方形，其中 left 表示该方块最左边的点位置(positions[i][0])，side_length 表示该方块的边长(positions[i][1])。

每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。

方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。邻接掉落的边不会过早地粘合在一起，因为只有底边才具有粘性。

 

返回一个堆叠高度列表 ans 。每一个堆叠高度 ans[i] 表示在通过 positions[0], positions[1], ..., positions[i] 表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。

 

 

示例 1:

输入: [[1, 2], [2, 3], [6, 1]]
输出: [2, 5, 5]
解释:

第一个方块 positions[0] = [1, 2] 掉落：
_aa
_aa
-------
方块最大高度为 2 。

第二个方块 positions[1] = [2, 3] 掉落：
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
方块最大高度为5。
大的方块保持在较小的方块的顶部，不论它的重心在哪里，因为方块的底部边缘有非常大的粘性。

第三个方块 positions[1] = [6, 1] 掉落：
__aaa
__aaa
__aaa
_aa
_aa___a
--------------
方块最大高度为5。

因此，我们返回结果[2, 5, 5]。
 

示例 2:

输入: [[100, 100], [200, 100]]
输出: [100, 100]
解释: 相邻的方块不会过早地卡住，只有它们的底部边缘才能粘在表面上。
 

注意:

1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/falling-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1普通方法
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        m = [0] * len(positions)
        for i in range(len(positions)):
            l, length = positions[i]
            r = l + length - 1
            for j in range(i + 1, len(positions)):
                l_j, length_j = positions[j]
                r_j = l_j + length_j - 1
                if l_j <= r and l <= r_j:
                    m[j] = max(length + m[i], m[j])  # m[i]+length代表被i_方块影响后的j,取max的意思可以看案例1，因为只有之前最高的可以卡住，其他在谷里的是不用考虑的因为卡不住
            m[i] += length
        ans = []
        for i in range(len(m)):
            if not ans or m[i] > ans[-1]:
                ans.append(m[i])
            else:
                ans.append(ans[-1])
        return ans


# 案例1 [[50,47],[95,48],[88,77],[84,3],[3,87]]


# 2坐标压缩 坐标离散化
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        m = set()
        for i in range(len(positions)):
            l, r = positions[i][0], positions[i][0] + positions[i][1] - 1
            m |= {l, r}
        m = sorted(list(m))
        index = {x: i for i, x in enumerate(m)}
        a = [0] * len(index)
        ans = []
        flag = 0
        for l, length in positions:
            L = index[l]
            R = index[l + length - 1]
            x = max(a[L:R + 1])  # x为当前区间可以卡住的最大值
            for i in range(L, R + 1):
                a[i] = x + length
            flag = max(flag, x + length)  # flag为遍历至当前目标的最大值
            ans.append(flag)
        return ans


# https://leetcode-cn.com/problems/falling-squares/solution/diao-luo-de-fang-kuai-by-leetcode/
# 方法3 方块（平方根）分解 sqrt分解
# 相当于分了两个块，blocks_read代表L-R边缘所在区的最高高度，blocks则代表完整第i块的最高高度，update的时候只有L-R完整跨越一个block才更新blocks[i]，而对于不完整跨越的边缘区如(L,R)则更新blocks_read[i];而到了query时则反过来了，检测到L-R边缘在block区就获取block，而需要完整跨越blocks_read才获取blocks_read的值
class Solution(object):
    def fallingSquares(self, positions):
        # Coordinate compression
        # index = ...
        m = set()
        for i in range(len(positions)):
            l, r = positions[i][0], positions[i][0] + positions[i][1] - 1
            m |= {l, r}
        m = sorted(list(m))
        index = {x: i for i, x in enumerate(m)}
        W = len(index)
        B = int(W ** .5)
        heights = [0] * W
        blocks = [0] * (B + 2)
        blocks_read = [0] * (B + 2)

        def query(left, right):
            ans = 0
            while left % B and left <= right:
                ans = max(ans, heights[left], blocks[left // B])
                left += 1
            while right % B != B - 1 and left <= right:
                ans = max(ans, heights[right], blocks[right // B])
                right -= 1
            while left <= right:
                ans = max(ans, blocks[left // B], blocks_read[left // B])
                left += B
            return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left // B] = max(blocks_read[left // B], h)
                left += 1
            while right % B != B - 1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right // B] = max(blocks_read[right // B], h)
                right -= 1
            while left <= right:
                blocks[left // B] = max(blocks[left // B], h)
                left += B

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans


# 方法4 线段树+惰性传播 懒惰传播
import collections


class Solution(object):
    def __init__(self):
        self.tree = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)

    def fallingSquares(self, positions):
        m = set()
        for i in range(len(positions)):
            l, r = positions[i][0], positions[i][0] + positions[i][1] - 1
            m |= {l, r}
        m = sorted(list(m))
        index = {x: i for i, x in enumerate(m)}

        def query(s, e, l, r, id):
            if s >= r or l >= e:
                return 0
            if s <= l < r <= e:
                return self.tree[id]
            else:
                mid = (l + r) // 2
                return max(self.lazy[id],query(s, e, l, mid, 2 * id + 1), query(s, e, mid, r,2 * id + 2))

        def update(s, e, l, r, h, id=0):
            if s >= r or l >= e:
                return
            if s <= l < r <= e:
                self.tree[id] = max(h, self.tree[id])
                self.lazy[id] = max(h, self.tree[id])
            else:
                mid = (l + r) // 2
                update(s, e, l, mid, h, 2 * id + 1)
                update(s, e, mid, r, h, 2 * id + 2)
                self.tree[id] = max(self.lazy[id], max(self.tree[2 * id + 1], self.tree[2 * id + 2]))

        ans = []
        for l, length in positions:
            L = index[l]
            R = index[l + length - 1]
            h = query(L, R + 1, 0, len(index), 0) + length
            update(L, R + 1, 0, len(index), h, 0)
            ans.append(self.tree[0])
        return ans


Solution().fallingSquares([[9, 7], [1, 9], [3, 1]])
