# -*- coding: utf-8 -*-
import collections
from typing import List


# 你是一只蚂蚁，负责为蚁群构筑 n 间编号从 0 到 n-1 的新房间。给你一个 下标从 0 开始 且长度为 n 的整数数组 prevRoom 作为扩建计划。其中，prevRoom[i] 表示在构筑房间 i 之前，你必须先构筑房间 prevRoom[i] ，并且这两个房间必须 直接 相连。房间 0 已经构筑完成，所以 prevRoom[0] = -1 。扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 0 可以访问到每个房间。
#
# 你一次只能构筑 一个 房间。你可以在 已经构筑好的 房间之间自由穿行，只要这些房间是 相连的 。如果房间 prevRoom[i] 已经构筑完成，那么你就可以构筑房间 i。
#
# 返回你构筑所有房间的 不同顺序的数目 。由于答案可能很大，请返回对 109 + 7 取余 的结果。
#
#  
#
# 示例 1：
#
#
# 输入：prevRoom = [-1,0,1]
# 输出：1
# 解释：仅有一种方案可以完成所有房间的构筑：0 → 1 → 2
# 示例 2：
#
#
# 输入：prevRoom = [-1,0,0,1,2]
# 输出：6
# 解释：
# 有 6 种不同顺序：
# 0 → 1 → 3 → 2 → 4
# 0 → 2 → 4 → 1 → 3
# 0 → 1 → 2 → 3 → 4
# 0 → 1 → 2 → 4 → 3
# 0 → 2 → 1 → 3 → 4
# 0 → 2 → 1 → 4 → 3
#  
#
# 提示：
#
# n == prevRoom.length
# 2 <= n <= 105
# prevRoom[0] == -1
# 对于所有的 1 <= i < n ，都有 0 <= prevRoom[i] < n
# 题目保证所有房间都构筑完成后，从房间 0 可以访问到每个房间
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-ways-to-build-rooms-in-an-ant-colony
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10 * 9 + 7
        graph = collections.defaultdict(list)
        for i, pre in enumerate(prevRoom[1:], 1):
            graph[pre].append(i)
        dp = collections.defaultdict(int)
        dp[0] = 1
        nums = collections.defaultdict(lambda:1)

        def num(node):
            if not graph[node]:
                return 1
            ans = 1
            for nxt in graph[node]:
                ans += num(nxt)
            nums[node] = ans
            return ans

        num(0)

        def dfs(node):
            if not graph[node]:
                return 1
            li = []
            for nxt in graph[node]:
                li.append(dfs(nxt))
            prefix = [1]
            for n in li:
                prefix.append(prefix[-1] * n)
            ans = 0
            for i, nxt in enumerate(graph[node]):
                ans += ((prefix[-1]//prefix[i])*nums[nxt])%mod
            ans%=mod
            return ans
        return dfs(0)
Solution().waysToBuildRooms([-1,0,1])