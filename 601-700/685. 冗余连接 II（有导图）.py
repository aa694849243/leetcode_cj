'''在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。

输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。

返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

 

示例 1：


输入：edges = [[1,2],[1,3],[2,3]]
输出：[2,3]
示例 2：


输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
输出：[4,1]
 

提示：

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        parent = collections.defaultdict(lambda:-1)
        conflict = -1
        cycle = -1
        for i, (x, y) in enumerate(edges):
            if parent[y] != -1:
                conflict = i
            else:
                parent[y] = x
                if find(y) != find(x):
                    union(x, y)
                else:
                    cycle = i  # 成环边为遍历最后一条的环中边
        if conflict < 0:  # 只有成环边
            return [edges[cycle][0], edges[cycle][1]]
        else:
            if cycle < 0:  # 只有冲突边
                return [edges[conflict][0], edges[conflict][1]]
            else:  # 既有冲突边，又有成环边
                nonmarkconflict_0 = parent[edges[conflict][1]]
                return [nonmarkconflict_0, edges[conflict][1]]

