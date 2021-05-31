# 在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。
#
#  现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。
#
#  在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
#
#  示例：
#
#  输入：["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,1
# 5,20,25,30]],[3],[12],[25],[15],[24],[8]]
# 输出：[null,0,1,1,0,0,1]
# 解释：
# 时间为 3，票数分布情况是 [0]，编号为 0 的候选人领先。
# 时间为 12，票数分布情况是 [0,1,1]，编号为 1 的候选人领先。
# 时间为 25，票数分布情况是 [0,1,1,0,0,1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。
# 在时间 15、24 和 8 处继续执行 3 个查询。
#
#
#
#
#  提示：
#
#
#  1 <= persons.length = times.length <= 5000
#  0 <= persons[i] <= persons.length
#  times 是严格递增的数组，所有元素都在 [0, 10^9] 范围中。
#  每个测试用例最多调用 10000 次 TopVotedCandidate.q。
#  TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。
#
#  Related Topics 二分查找
#  👍 37 👎 0

from typing import List

import collections
import bisect


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        ma = 0
        C = collections.Counter()
        res = []
        for i, id in enumerate(persons):
            C[id] += 1
            if C[id] >= ma:
                ma = C[id]
                res.append(id)
            else:
                res.append(res[-1])
        self.p = res
        self.times = times

    def q(self, t: int) -> int:
        i = bisect.bisect_left(self.times, t)
        if i == len(self.times):
            return self.p[-1]
        elif i == 0:
            if self.times[i] > t:
                return
            else:
                return self.p[0]
        else:
            if self.times[i] == t:
                return self.p[i]
            else:
                return self.p[i - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
