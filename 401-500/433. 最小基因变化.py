'''一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:

起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。
示例 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

返回值: 1
示例 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

返回值: 2
示例 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

返回值: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-genetic-mutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1深度优先遍历
class Solution:
    def __init__(self):
        self.mincnt = float('inf')
        self.bank = []
        self.m = {'A': 'GCT', 'G': 'ACT', 'C': 'AGT', 'T': 'AGC'}

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        self.bank = set(bank)
        self.mincnt = len(bank) + 1
        n = self.mincnt
        if end not in bank:
            return -1

        def dfs(cur, cnt):
            if cnt >= self.mincnt:
                return
            if cur == end:
                self.mincnt = min(self.mincnt, cnt)
                return
            for i in range(len(cur)):
                for j in self.m[cur[i]]:
                    new = cur[:i] + j + cur[i + 1:]
                    if new not in self.bank:
                        continue
                    self.bank.discard(new)
                    dfs(new, cnt + 1)
                    self.bank.add(new)

        dfs(start, 0)
        return self.mincnt if self.mincnt < n else -1


# 2双向广度优先遍历


class Solution:
    def __init__(self):
        self.mincnt = float('inf')
        self.m = {'A': 'GCT', 'G': 'ACT', 'C': 'AGT', 'T': 'AGC'}

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        startbank = {start}
        endbank = {end}
        bank = set(bank)
        bank.discard(start)
        cnt = 0
        while startbank:
            cnt += 1
            m = set()
            for a in startbank:
                for i, s in enumerate(a):
                    for j in self.m[s]:
                        new = a[:i] + j + a[i + 1:]
                        if new in endbank:
                            return cnt
                        if new in bank:
                            m.add(new)
                            bank.discard(new)
            startbank = m
            if len(startbank) > len(endbank):
                endbank, startbank = startbank, endbank
        return -1


a = "AAAACCCC"
b = "CCCCCCCC"
c = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
Solution().minMutation(a, b, c)
