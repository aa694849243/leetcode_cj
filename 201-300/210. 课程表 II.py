'''
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
from collections import deque


# 深度优先遍历 dfs
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edge = defaultdict(list)
        vs = [0] * numCourses
        valid = True
        res = []
        for info in prerequisites:
            edge[info[1]].append(info[0])

        def dfs(vi):
            nonlocal valid
            vs[vi] = 1
            for v in edge[vi]:
                if vs[v] == 0 and valid:
                    dfs(v)
                elif vs[v] == 1:
                    valid = False
            vs[vi] = 2
            res.append(vi)

        for vi in range(numCourses):
            if vs[vi] == 0:
                dfs(vi)
        res.reverse()
        return res if valid else []


# 宽度优先遍历 bfs
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edge = defaultdict(list)
        ingree = [0] * numCourses
        res = []
        for info in prerequisites:
            edge[info[1]].append(info[0])
            ingree[info[0]] += 1
        que = deque([i for i in range(numCourses) if ingree[i] == 0])
        while que:
            v = que.popleft()
            res.append(v)
            for i in edge[v]:
                ingree[i] -= 1
                if ingree[i] == 0:
                    que.append(i)
        return res if len(res)==numCourses else []


n = 2
l = [[1, 0]]
Solution().findOrder(n, l)
