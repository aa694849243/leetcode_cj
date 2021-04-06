'''给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
给定：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
返回：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= equations[i][0].length, equations[i][1].length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= queries[i][0].length, queries[i][1].length <= 5
equations[i][0], equations[i][1], queries[i][0], queries[i][1] 由小写英文字母与数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 1 图 dfs 深度优先遍历
from typing import List
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for i, (e1, e2) in enumerate(equations):
            graph[e1][e2] = values[i]
            graph[e2][e1] = 1 / values[i]
        mem = set()

        def dfs(v1, v2, co):
            if v1 not in graph or v2 not in graph:
                return -1.0
            if v1 == v2:
                return 1.0
            if v2 in graph[v1]:
                return co * graph[v1][v2]
            if v1 in mem:
                return -1.0
            mem.add(v1)
            a = -1
            for v in graph[v1]:
                m = dfs(v, v2, co * graph[v1][v])
                a = m if m > 0 else a
            mem.discard(
                v1)  # 每一步添加之后再去掉是标准做法，但因为这里每一条路都会有一个答案，即每个节点要么通到最终路径要么返回-1，所以加入的所有节点都不用重复考虑，所以可以直接在起始位置初始化就好了，如别人答案做法
            return a

        ans = []
        for i in range(len(queries)):
            ans.append(dfs(queries[i][0], queries[i][1], 1))
        return ans


equations = [["a", "b"], ["b", "c"], ["a", "c"], ["d", "e"]]
values = [2.0, 3.0, 6.0, 1.0]
queries = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"], ["a", "d"]]

Solution().calcEquation(equations=equations, values=values, queries=queries)


##1 别人答案
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构造图，equations的第一项除以第二项等于value里的对应值，第二项除以第一项等于其倒数
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        # dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
        def dfs(s, t) -> int:
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)  # 添加到已访问避免重复遍历
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        # 逐个计算query的值
        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res


# 2 图 bfs 宽度优先遍历
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for i, (e1, e2) in enumerate(equations):
            graph[e1][e2] = values[i]
            graph[e2][e1] = 1 / values[i]
        res = []
        for i in range(len(queries)):
            if queries[i][0] not in graph or queries[i][1] not in graph:
                res.append(-1.0)
                continue
            if queries[i][0] == queries[i][1]:
                res.append(1.0)
                continue
            que = collections.deque()
            que.append((queries[i][0], 1))
            mem = {queries[i][0]}
            ans = -1.0
            while que:
                v1, co = que.popleft()
                if v1 == queries[i][1]:
                    ans = co
                    break
                for v2 in graph[v1]:
                    if v2 in mem:
                        continue
                    mem.add(v2)
                    que.append((v2, co * graph[v1][v2]))
            res.append(ans)
        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

Solution().calcEquation(equations=equations, values=values, queries=queries)

# 3 图+并查集
# https://leetcode-cn.com/problems/evaluate-division/solution/python3-bing-cha-ji-qiu-jie-by-zengjianlin-2/
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        f = {}
        d = {}  # 每个节点对根值的倍数
        res = []

        def find(x):
            f.setdefault(x, x)
            d.setdefault(x, 1)
            if f[x] != x:
                t=f[x]
                f[x] = find(f[x])
                d[x] *= d[t]
            return f[x]

        def union(x, y, co):
            a, b = find(x), find(y)
            if a != b:
                f[b] = find(a)
                d[b] = co*d[x]/d[y]

        def check(v1, v2):
            if v1 not in f or v2 not in f:
                return -1.0
            if find(v1) != find(v2):
                return -1.0
            return d[v1] / d[v2]

        for i in range(len(equations)):
            a = find(equations[i][0])
            b = find(equations[i][1])
            union(b, a, values[i])
        for i in range(len(queries)):
            res.append(check(queries[i][0], queries[i][1]))
        return res

# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         f = {}
#         d = {}
#
#         def find(x):
#             f.setdefault(x, x)
#             d.setdefault(x,1)
#             if x != f[x]:
#                 t = f[x]
#                 f[x] = find(t)
#                 d[x] *= d[t]
#                 return f[x]
#             return x
#
#         def union(A, B, value):
#             a, b = find(A), find(B)
#             if a != b:
#                 f[a] = b
#                 d[a] = d[B] / d[A] * value
#
#         def check(x, y):
#             if x not in f or y not in f:
#                 return -1.0
#             a, b = find(x), find(y)
#             if a != b:
#                 return -1.0
#             return d[x] / d[y]
#
#         for i, nums in enumerate(equations):
#             union(nums[0], nums[1], values[i])
#         res = []
#         for x, y in queries:
#             res.append(check(x, y))
#         return res

equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
values = [3.0, 4.0, 5.0, 6.0]
queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]

Solution().calcEquation(equations=equations, values=values, queries=queries)

# 4 Floyd
# https://leetcode-cn.com/problems/evaluate-division/solution/399chu-fa-qiu-zhi-floydsuan-fa-qiu-duo-yuan-lu-jin/
import itertools


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        matrix = {}
        for i in range(len(equations)):  # 构建矩阵
            matrix[(equations[i][0], equations[i][1])] = values[i]
            matrix[(equations[i][1], equations[i][0])] = 1 / values[i]
        vnums = list(set(itertools.chain.from_iterable(equations)))  # 列表扁平化
        size = len(vnums)
        dp = [[float('inf')] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if i == j:
                    dp[i][j] = 1
                else:
                    if (vnums[i], vnums[j]) in matrix:
                        dp[i][j] = matrix[(vnums[i], vnums[j])]

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if dp[i][k] * dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] * dp[k][j]
        for i in range(len(queries)):
            if queries[i][0] not in vnums or queries[i][1] not in vnums:
                res.append(-1.0)
                continue
            v1 = vnums.index(queries[i][0])
            v2 = vnums.index(queries[i][1])
            num = -1.0 if dp[v1][v2] == float('inf') else dp[v1][v2]
            res.append(num)
        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

Solution().calcEquation(equations=equations, values=values, queries=queries)
