# -*- coding: utf-8 -*-
# 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。
#
#  员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会
# 是他自己。
#
#  给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。
#
#
#
#
#  示例 1：
#
#
#
#  输入：favorite = [2,2,1,2]
# 输出：3
# 解释：
# 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
# 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
# 注意，公司也可以邀请员工 1，2 和 3 参加会议。
# 所以最多参加会议的员工数目为 3 。
#
#
#  示例 2：
#
#  输入：favorite = [1,2,0]
# 输出：3
# 解释：
# 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
# 座位安排同图 1 所示：
# - 员工 0 坐在员工 2 和 1 之间。
# - 员工 1 坐在员工 0 和 2 之间。
# - 员工 2 坐在员工 1 和 0 之间。
# 参与会议的最多员工数目为 3 。
#
#
#  示例 3：
#
#
#
#  输入：favorite = [3,0,1,4,1]
# 输出：4
# 解释：
# 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
# 员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
# 所以公司只能不邀请员工 2 。
# 参加会议的最多员工数目为 4 。
#
#
#
#
#  提示：
#
#
#  n == favorite.length
#  2 <= n <= 10⁵
#  0 <= favorite[i] <= n - 1
#  favorite[i] != i
#
#
#  Related Topics 深度优先搜索 图 拓扑排序
#  👍 66 👎 0
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/solution/can-jia-hui-yi-de-zui-duo-yuan-gong-shu-u8e8u/
# 基环内向树
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for i, fa in enumerate(favorite):
            indegree[fa] += 1
        q = collections.deque()
        for i, ind in enumerate(indegree):
            if ind == 0:
                q.append(i)
        visted = set()
        f = [1] * n
        while q:
            node = q.popleft()
            visted.add(node)
            nxt = favorite[node]
            f[nxt] = max(f[nxt], f[node] + 1)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
        ring, twod = 0, 0
        res = 0
        for i in range(n):
            if i not in visted:
                if favorite[favorite[i]] == i:
                    visted |= {i, favorite[i]}
                    twod += f[i] + f[favorite[i]]
                else:
                    cnt = 1
                    cur = i
                    visted.add(cur)
                    while favorite[cur] not in visted:
                        cnt += 1
                        cur = favorite[cur]
                        visted.add(cur)
                    ring = max(cnt, ring)
        return max(ring,twod)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maximumInvitations([21,12,1,7,5,6,20,2,14,15,12,14,2,20,0,17,23,12,17,13,11,13,3,11]))
