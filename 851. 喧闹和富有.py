# 在一组 N 个人（编号为 0, 1, 2, ..., N-1）中，每个人都有不同数目的钱，以及不同程度的安静（quietness）。
#
#  为了方便起见，我们将编号为 x 的人简称为 "person x "。
#
#  如果能够肯定 person x 比 person y 更有钱的话，我们会说 richer[i] = [x, y] 。注意 richer 可能只是有效观察的
# 一个子集。
#
#  另外，如果 person x 的安静程度为 q ，我们会说 quiet[x] = q 。
#
#  现在，返回答案 answer ，其中 answer[x] = y 的前提是，在所有拥有的钱不少于 person x 的人中，person y 是最安静的人
# （也就是安静值 quiet[y] 最小的人）。
#
#  示例：
#
#  输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1
# ,7,0]
# 输出：[5,5,2,5,4,5,6,7]
# 解释：
# answer[0] = 5，
# person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
#
# 唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
# 但是目前还不清楚他是否比 person 0 更有钱。
#
# answer[7] = 7，
# 在所有拥有的钱肯定不少于 person 7 的人中(这可能包括 person 3，4，5，6 以及 7)，
# 最安静(有较低安静值 quiet[x])的人是 person 7。
#
# 其他的答案也可以用类似的推理来解释。
#
#
#  提示：
#
#
#  1 <= quiet.length = N <= 500
#  0 <= quiet[i] < N，所有 quiet[i] 都不相同。
#  0 <= richer.length <= N * (N-1) / 2
#  0 <= richer[i][j] < N
#  richer[i][0] != richer[i][1]
#  richer[i] 都是不同的。
#  对 richer 的观察在逻辑上是一致的。
#
#  Related Topics 深度优先搜索
#  👍 49 👎 0


from typing import List
import collections


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        m = collections.defaultdict(list)
        for x, y in richer:
            m[y].append(x)
        dp = [-1] * len(quiet)

        def solve(node):
            t = [node]
            res = []
            while True:
                tree = []
                for nxt in t:
                    if dp[nxt] != -1:
                        res.append(dp[nxt])
                        continue
                    res.append(nxt)
                    tree.extend(m[nxt])
                if not tree:
                    break
                t = tree
            a = min(res, key=lambda i: quiet[i])
            dp[node] = a

        for node in range(len(quiet)):
            solve(node)
        return dp


Solution().loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet=[3, 2, 5, 4, 6, 1, 7, 0])
