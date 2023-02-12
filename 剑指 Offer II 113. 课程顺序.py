# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 21:38 
# ide： PyCharm
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        degrees = [0] * numCourses
        for u, v in prerequisites:
            degrees[u] += 1
            g[v].append(u)
        visted = [False] * numCourses
        res = []
        pq = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                pq.append(i)
                res.append(i)
        while pq:
            u = pq.popleft()
            for v in g[u]:
                degrees[v] -= 1
                if degrees[v] == 0:
                    pq.append(v)
                    res.append(v)
        return res if len(res) == numCourses else []

# leetcode submit region end(Prohibit modification and deletion)

