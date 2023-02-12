# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 22:22 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import collections
from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        m = set()
        g = collections.defaultdict(set)
        degrees = [0] * 26
        for i, word in enumerate(words):
            m |= set(word)
            for j in range(i):
                pre = words[j]
                for k in range(min(len(pre), len(word))):
                    if pre[k] != word[k]:
                        if pre[k] in g[word[k]]:
                            return ""
                        elif word[k] in g[pre[k]]:
                            break
                        g[pre[k]].add(word[k])
                        degrees[ord(word[k]) - ord('a')] += 1
                        break
                else:
                    if len(pre) > len(word):
                        return ""
        pq = deque()
        for i, c in enumerate(degrees):
            if c == 0 and chr(i + ord('a')) in m:
                pq.append(chr(i + ord('a')))
        ans = []
        while pq:
            c = pq.popleft()
            ans.append(c)
            for nxt in g[c]:
                degrees[ord(nxt) - ord('a')] -= 1
                if degrees[ord(nxt) - ord('a')] == 0:
                    pq.append(nxt)
        return "".join(ans) if len(ans) == len(m) else ""


# leetcode submit region end(Prohibit modification and deletion)

print(
    Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
)

