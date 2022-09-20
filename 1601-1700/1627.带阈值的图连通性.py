from typing import List


# @solution-sync:begin
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a > b:
                a, b = b, a
            if a != b:
                f[b] = a

        for i in range(threshold + 1, n + 1):
            for j in range(2 * i, n + 1, i):
                union(i, j)
        res = []
        for x, y in queries:
            res.append(find(x) == find(y))
        return res


# @solution-sync:end
print(Solution().areConnected(26, 3, [[16, 12], [16, 9]]))
