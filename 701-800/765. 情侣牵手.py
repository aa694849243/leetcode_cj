'''N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

示例 1:

输入: row = [0, 2, 1, 3]
输出: 1
解释: 我们只需要交换row[1]和row[2]的位置即可。
示例 2:

输入: row = [3, 2, 0, 1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。
说明:

len(row) 是偶数且数值在 [4, 60]范围内。
可以保证row 是序列 0...len(row)-1 的一个全排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/couples-holding-hands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1贪心 异或妙用
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        cnt = 0
        for i in range(len(row) - 1, step=2):
            if row[i] == row[i + 1] ^ 1:
                continue
            for j in range(i + 1, len(row)):
                if row[j] == row[i] ^ 1:
                    row[j], row[i + 1] = row[i + 1], row[j]
                    cnt += 1
        return cnt


# 1优化，以空间换时间
import collections


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        m = collections.defaultdict(int)
        for i, val in enumerate(row):
            m[val] = i
        cnt = 0
        for i in range(0, len(row) - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                continue
            else:
                cnt += 1
                j = m[row[i] ^ 1]
                m[row[i + 1]] = j  # 将i+1的值储存的位置改为j
                row[i + 1], row[j] = row[j], row[i + 1]
        return cnt


# 2并查集 找连通分量个数写法
# 将正确位置编号0，1编一，2，3编二。。。编号相同的视为一个节点，寻找总的连通分量
class Solution:
    cnt = 0

    def minSwapsCouples(self, row: List[int]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            # f[find(y)] = find(x)
            t1, t2 = find(x), find(y)
            if t1 != t2:
                f[t2] = t1
                self.cnt += 1

        for i in range(0, len(row) - 1, 2):
            union(row[i + 1] // 2, row[i] // 2)
        # r = collections.defaultdict(int)
        # for num in range(len(row) // 2):
        #     r[f[num]] += 1
        # ans = 0
        # for i in r:
        #     ans += r[i] - 1
        return self.cnt


# 并查集，求源点做法
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        for i in range(0, len(row) - 1, 2):
            union(row[i + 1] // 2, row[i] // 2)
        r = collections.defaultdict(int)
        for num in range(len(row) // 2):
            r[find(num)] += 1
        ans = 0
        for i in r:
            ans += r[i] - 1
        return ans


# dfs
class Solution:
    def __init__(self):
        self.cnt = 0
        self.loop = collections.defaultdict(set)

    def minSwapsCouples(self, row: List[int]) -> int:

        def dfs(node):
            if node in m:
                return
            m.add(node)
            for node2 in self.loop[node]:
                dfs(node2)

        for i in range(0, len(row) - 1, 2):
            node1, node2 = row[i] // 2, row[i + 1] // 2
            self.loop[node1].add(node2)
            self.loop[node2].add(node1)
        m = set()
        for node in range(len(row) // 2):
            if node not in m:
                dfs(node)
            else:
                self.cnt += 1
        return self.cnt


# bfs
class Solution:
    def __init__(self):
        self.cnt = 0
        self.loop = collections.defaultdict(set)

    def minSwapsCouples(self, row: List[int]) -> int:
        for i in range(0, len(row) - 1, 2):
            node1, node2 = row[i] // 2, row[i + 1] // 2
            self.loop[node1].add(node2)
            self.loop[node2].add(node1)
        m = set()
        for root in range(len(row) // 2):
            if root in m:
                self.cnt += 1
                continue
            t = [root]
            while True:
                tree = []
                for node in t:
                    for nxtnode in self.loop[node]:
                        if nxtnode not in m:
                            m.add(nxtnode)
                            tree.append(nxtnode)
                if not tree:
                    break
                t = tree
        return self.cnt


Solution().minSwapsCouples([5, 4, 2, 6, 3, 1, 0, 7])
