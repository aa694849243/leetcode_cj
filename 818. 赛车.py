# 你的赛车起始停留在位置 0，速度为 +1，正行驶在一个无限长的数轴上。（车也可以向负数方向行驶。）
#
#  你的车会根据一系列由 A（加速）和 R（倒车）组成的指令进行自动驾驶 。
#
#  当车得到指令 "A" 时, 将会做出以下操作： position += speed, speed *= 2。
#
#  当车得到指令 "R" 时, 将会做出以下操作：如果当前速度是正数，则将车速调整为 speed = -1 ；否则将车速调整为 speed = 1。 (当前所
# 处位置不变。)
#
#  例如，当得到一系列指令 "AAR" 后, 你的车将会走过位置 0->1->3->3，并且速度变化为 1->2->4->-1。
#
#  现在给定一个目标位置，请给出能够到达目标位置的最短指令列表的长度。
#
#  示例 1:
# 输入:
# target = 3
# 输出: 2
# 解释:
# 最短指令列表为 "AA"
# 位置变化为 0->1->3
#
#
#  示例 2:
# 输入:
# target = 6
# 输出: 5
# 解释:
# 最短指令列表为 "AAARA"
# 位置变化为 0->1->3->7->7->6
#
#
#  说明:
#
#
#  1 <= target（目标位置） <= 10000。
#
#  Related Topics 堆 动态规划
#  👍 95 👎 0
import heapq


# 1dijsktra
class Solution(object):
    def racecar(self, target):
        K = target.bit_length()
        one_distance = 1 << K  # 一次能走的最远距离，假如target=5一次最远走8,累积最长走16
        barrier = 1 << (K + 1)
        distances = [float('inf')] * (2 * barrier + 1)  # 一个小知识，如果列表长度为奇数，distance[x]!=distance[-x]
        distances[target] = 0  # distances[i]代表距离目标距离为i，val为用的最少步数
        q = [(0, target)]
        while q:
            steps, tr = heapq.heappop(q)
            # if distances[tr] < steps:  # 如果distance[tr]<steps，说明已经有更早的步数到达tr了，不必再重复访问了
            #     continue
            if tr == 0:
                return steps
            for k in range(K + 1):
                walk = 2 ** k - 1  # 走了walk步，记为A^kR，R为转向
                tr2 = walk - tr  # 如果walk超过tr，经过一次R转向后，下一次走依旧是正向，如果walk没超过tr，提早转向了，后面走就是背道而驰，tr2就为负数
                nxt_steps = steps + k + 1  # 因为每次的步长最少都是1
                if tr2 == 0:
                    nxt_steps -= 1  # 如果已经到达目的地了，少一个R字段
                if abs(tr2) <= barrier and distances[tr2] > nxt_steps:
                    distances[tr2] = nxt_steps
                    heapq.heappush(q, (nxt_steps, tr2))


# 2动态规划
class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * (target - 2)
        for t in range(3, target + 1):  # 两种情况 1 A^k-1R未到达目的地，折返A^jR后再跑到t
            k = t.bit_length()  # 2  A^kR超过目的地折返
            if t == 2 ** k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2 ** (k - 1) + 2 ** j] + k - 1 + j + 2)
            if 2 ** k - 1 - t < t:  # 回滚距离小于t
                dp[t] = min(dp[t], dp[2 ** k - 1 - t] + k + 1)
        return dp[target]


Solution().racecar(6)
