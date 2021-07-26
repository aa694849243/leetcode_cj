# -*- coding: utf-8 -*-
from typing import List


# 为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球
# 在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，
# 小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不
# 能再向左弹。
#
#  为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。
#
#  示例 1：
#
#
#  输入：jump = [2, 5, 1, 1, 1, 1]
#
#  输出：3
#
#  解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。
#
#
#  限制：
#
#
#  1 <= jump.length <= 10^6
#  1 <= jump[i] <= 10000
#
#  Related Topics 广度优先搜索 线段树 数组 动态规划
#  👍 52 👎 0

# 1dp
class Solution:
    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        f = [n] * (n + 1)
        f[0] = 0
        maxdis = [0] * (n + 1)
        curstep = 0
        ans = n
        for i, val in enumerate(jump):
            if i > maxdis[curstep]:  # 目前的步数到达最远的地方,如果当前步数到达不了i，那么增加一步，因为curstep至少可以到达i-1，所以curstep+1一定可以到达或超越i
                curstep += 1
            f[i] = min(f[i], curstep + 1)  # 假如maxdis[step]超越i，则等式成立，如果maxdis[step]==i,说明之前至少将f[i]更新为step了
            nxtjump = i + val
            if i + val >= n:
                ans = min(f[i] + 1, ans)
            else:
                maxdis[f[i] + 1] = max(nxtjump, maxdis[f[i] + 1])  # 到达f[i]的最小步数+1后即可更新下一个step的最长距离
                # 每次更新的都是下一步或下两步的最大距离，所以当前轮次的最远距离不会被改变。又因为curstep+1步假如比curstep+2步跳的更远的话，遍历到curstep+1步时就会及时更新curstep+2步的值
                f[nxtjump] = min(f[nxtjump], f[i] + 1)
        return ans


class Solution:
    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        step = 0
        t = [0]
        far = 1
        visted = [False] * (n + 1)
        visted[0]=True
        while True:
            tree = []
            for i in t:
                e = jump[i] + i
                if e >= n:
                    return step+1
                for nxt in range(far, i):
                    if not visted[nxt]:
                        tree.append(nxt)
                        visted[nxt]=True
                if not visted[e]:
                    visted[e]=True
                    tree.append(e)
                far=max(i+1,far)
            step+=1
            t=tree



Solution().minJump([3, 7, 6, 1, 4, 3, 7, 8, 1, 2])
